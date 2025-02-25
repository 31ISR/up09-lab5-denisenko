from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    name = models.CharField('Заголовок', max_length=75)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    description = models.TextField('Описание',max_length=150)
    slug = models.SlugField('Служебный код')
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField('Свободный вход')
    banner = models.ImageField('Картинка',default='fallback.png', blank=True)

    def __str__(self):
        return self.name
# Create your models here.
