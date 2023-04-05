from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class User(models.Model):
    first_name = models.CharField(
        validators=[RegexValidator(
            regex='[A-Z]{1}[a-z]*', message='Invalid name format')],
        max_length=14
    )
    last_name = models.CharField(
        validators=[RegexValidator(
            regex='[A-Z]{1}[a-z]*', message='Invalid name format')],
        max_length=14
    )
    created_at = models.DateTimeField(auto_now_add=True)
