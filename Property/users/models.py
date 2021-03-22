from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


GENDER_CHOICES = [("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHER", "OTHER")]


class Person(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    date_of_birth = models.DateField()

    fiscal_id = models.IntegerField(default=0, null=True, blank=True)
    gender = models.CharField(max_length=64, choices=GENDER_CHOICES, null=True, blank=True)

    email = models.EmailField(max_length=255, unique=True, null=True, db_index=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], unique=True, max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "1 - Person"
        verbose_name_plural = "1 - Persons"


class Address(models.Model):
    line_1 = models.CharField(max_length=128, null=True, blank=True)
    line_2 = models.CharField(max_length=128, null=True, blank=True)
    county = models.CharField(max_length=128, null=True, blank=True)
    postcode = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} - {}'.format(self.postcode, self.country)

    class Meta:
        verbose_name = "2 - Address"
        verbose_name_plural = "2 - Addresses"


class User(AbstractUser):
    username = models.CharField(max_length=128, unique=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='Person', null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='Address', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True, blank=True)



    def __str__(self):
        return '{}'.format(self.username)

    class Meta:
        verbose_name = "3 - User"
        verbose_name_plural = "3 - Users"


PRIORITY_CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]


class ToDo(models.Model):
    user = models.ManyToManyField(User, related_name='users', symmetrical=True)
    #user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    priority = models.CharField(max_length=128, choices=PRIORITY_CHOICES, null=True, blank=True)

    due_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "4 - ToDo"
        verbose_name_plural = "4 - ToDos"