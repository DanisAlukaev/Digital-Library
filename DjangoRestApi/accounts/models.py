from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, image=None, mid_name=None):
        # Provide guidance for django backend on how regular users created.
        if image is not None:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password,
                              image=image, mid_name=mid_name)
        else:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password,
                              mid_name=mid_name)
        user.set_password(password)
        user.role = '2'
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, image=None, mid_name=None):
        # Provide guidance for django backend on how superuser created.
        if image is not None:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password,
                              image=image, mid_name=mid_name)
        else:
            user = self.model(email=email, first_name=first_name, last_name=last_name, password=password,
                              mid_name=mid_name)
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
    # Implement attributes of User entity according to ER schema.
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mid_name = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(max_length=1,
                            choices=[('0', 'administrator'), ('1', 'moderator'), ('2', 'regular')],
                            default='2'
                            )
    image = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default.png")
    # Create flags to keep track of application permissions.
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Specify required for registration attributes.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mid_name', 'image', 'role']
    USERNAME_FIELD = 'email'
    # Call user manager.
    objects = UserManager()

    def natural_key(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
