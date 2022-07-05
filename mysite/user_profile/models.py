from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        on_delete=models.CASCADE,
        verbose_name='vartotojas',
        related_name='profile',
    )
    picture = models.ImageField(
        'nuotrauka',
        default='user/profile/default.png',
        upload_to='user/profile/pictures',
    )

    def __str__(self):
        return '{} profile'.format(str(self.user))
