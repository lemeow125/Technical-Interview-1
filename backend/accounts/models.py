from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django_resized import ResizedImageField
import os


class CustomUser(AbstractUser):
    # first_name inherited from base user class
    # last_name inherited from base user class
    # email inherited from base user class
    # username inherited from base user class
    # password inherited from base user class
    # is_admin inherited from base user class

    avatar = models.ImageField(
        null=True, upload_to='avatars/')

    def avatar_url(self):
        return f'/api/v1/media/avatars/{self.avatar.name}'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def admin_url(self):
        return reverse('admin:users_customuser_change', args=(self.pk,))

    def get_prep_value(self, value):
        original_filename = self.avatar.field.storage.name(self.avatar.path)
        return original_filename
    pass


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'accounts':
        # Add test users here if needed
        # They will automatically be created after migrating the db
        users = [
            # Superadmin Account
            {
                'username': os.getenv('DJANGO_ADMIN_USERNAME'),
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_staff': True,
                'is_superuser': True,
                'first_name': 'Super',
                'last_name': 'Admin'
            },
            # Debug User
            {
                'username': 'debug-user',
                'email': os.getenv('DJANGO_ADMIN_EMAIL'),
                'password': os.getenv('DJANGO_ADMIN_PASSWORD'),
                'is_staff': False,
                'is_superuser': False,
                'first_name': "Test",
                'last_name': "User"
            },
        ]

        for user in users:
            if not CustomUser.objects.filter(username=user['username']).exists():
                if (user['is_superuser']):
                    USER = CustomUser.objects.create_superuser(
                        username=user['username'],
                        password=user['password'],
                        email=user['email'],
                    )
                    print('Created Superuser:', user['username'])
                else:
                    USER = CustomUser.objects.create_user(
                        username=user['username'],
                        password=user['password'],
                        email=user['email'],
                    )
                    print('Created User:', user['username'])
                USER.first_name = user['first_name']
                USER.last_name = user['last_name']
                USER.is_active = True
                USER.save()
