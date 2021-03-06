from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Title'),max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(_('Subject'),max_length=50)
    title = models.CharField(_('Title'),max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"
    
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('ToDo'),max_length=100)
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDo"