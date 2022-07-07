from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        related_name='profile',
    )
    picture = models.ImageField(
        _('picture'),
        default='user/profile/default.png',
        upload_to='user/profile/pictures',
    )

    def __str__(self):
        return _('{} profile').format(str(self.user))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        picture = Image.open(self.picture.path)
        if picture.height > 300 or picture.width > 300:
            output_size = (300, 300)
            picture.thumbnail(output_size)
            picture.save(self.picture.path)
