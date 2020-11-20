from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, degree, course, track, role=None, image=None, mid_name=None):
        # Provide guidance for django backend on how regular users created.
        if image is not None:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, image=image, mid_name=mid_name)
        else:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, mid_name=mid_name)
        user.set_password(password)
        user.role = '2'
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, degree, course, track, image=None, mid_name=None,
                         role=None):
        # Provide guidance for django backend on how superuser created.
        if image is not None:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, image=image, mid_name=mid_name)
        else:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password, degree=degree,
                              course=course, track=track, mid_name=mid_name)
        user.set_password(password)
        user.is_active = True
        user.role = '0'
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)


class User(AbstractBaseUser, PermissionsMixin):
    # Create auxiliary classes to explicitly specify options for position in UI.
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

    # Implement attributes of User entity according to ER schema.
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    # Name of a user.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mid_name = models.CharField(max_length=30, null=True, blank=True)
    # Position in IU.
    degree = models.IntegerField(choices=Degree.choices, default=0)
    course = models.IntegerField(choices=Course.choices, default=0)
    track = models.IntegerField(choices=Track.choices, default=0)
    # Role of a user.
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
    # Call user manager.
    objects = UserManager()

    def natural_key(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
