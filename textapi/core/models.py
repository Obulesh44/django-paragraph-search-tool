from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

 
# Custom user manager to handle user creation logic

class UserManager(BaseUserManager):
    def create_user(self, email, name, dob, password=None):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=self.normalize_email(email), name=name, dob=dob)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, dob, password):
        user = self.create_user(email, name, dob, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'dob']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    
# Paragraph model stores each paragraph of text submitted


class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()

# WordIndex maps each word to the paragraph it appears in


class WordIndex(models.Model):
    word = models.CharField(max_length=100)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='words')


