from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Class used to keep track of users. Implements methods for user and superuser creating.
    """

    def create_user(self, email, first_name, last_name, password, degree, course, track, role=None, image=None,
                    mid_name=None):
        # Provide guidance for django backend on how regular users are created.
        # Check whether image is provided.
        if image is not None:
            # Create a user with a specified profile image.
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, image=image, mid_name=mid_name)
        else:
            # Create a user with a default profile image.
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, mid_name=mid_name)
        # Set a password.
        user.set_password(password)
        # Role is regular.
        user.role = '2'

        # Django-required fields.
        # User is not a staff.
        user.is_staff = False
        # User is active.
        user.is_active = True
        # User is not a superuser.
        user.is_superuser = False
        # Save new user in database.
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, degree, course, track, image=None, mid_name=None,
                         role=None):
        # Provide guidance for django backend on how superuser created.
        # Check whether image is provided.
        if image is not None:
            # Create a user with a specified profile image.
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, image=image, mid_name=mid_name)
        else:
            # Create a user with a default profile image.
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, mid_name=mid_name)
        # Set a password.
        user.set_password(password)
        # Role is Administrator.
        user.role = '0'

        # Django-required fields.
        # User is a staff.
        user.is_staff = True
        # User is active.
        user.is_active = True
        # User is not a superuser.
        user.is_superuser = True
        # Save new user in database.
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Class used for authorization. Describes attributes of a user, e.g. email, first_name, last_name, mid_name, degree,
    course, track, role, image.
    """

    # Create auxiliary classes to explicitly specify options for a position in IU.
    class Degree(models.IntegerChoices):
        BACHELOR = 0
        MASTER = 1
        NOT_STUDENT = 2

    class Course(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4
        NOT_STUDENT = 5

    class Track(models.IntegerChoices):
        COMPUTER_SCIENCE = 0
        ROBOTICS = 1
        DATA_SCIENCE = 2
        SOFTWARE_ENGINEERING = 3
        SECURITY = 4
        NOT_STUDENT = 5

    # Implement attributes of User a entity according to ER schema.
    # Primary key email.
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    # Name of a user.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mid_name = models.CharField(max_length=30, null=True, blank=True)
    # Position in IU.
    degree = models.IntegerField(choices=Degree.choices, default=0)
    course = models.IntegerField(choices=Course.choices, default=0)
    track = models.IntegerField(choices=Track.choices, default=0)
    # Role of a user in the web-service.
    role = models.CharField(max_length=1,
                            choices=[('0', 'administrator'), ('1', 'moderator'), ('2', 'regular')],
                            default='2')
    # Profile picture.
    image = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default.png")
    # Create flags to keep track of application permissions.
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Specify required for registration attributes.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mid_name', 'image', 'role', 'degree', 'course', 'track']
    USERNAME_FIELD = 'email'
    # Call a user manager.
    objects = UserManager()

    def natural_key(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
