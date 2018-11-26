from django.db import models
from django.utils import timezone
# Create your models here.
class TodoItems(models.Model):
	content=models.TextField()
	status=models.PositiveSmallIntegerField(default=0)
	created_date=models.DateTimeField(default=timezone.now)

