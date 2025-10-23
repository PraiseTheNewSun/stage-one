from django.db import models

# Create your models here.
class StringModel(models.Model):
    id = models.IntegerField(default=0, unique=True, editable=False)
    value = models.CharField(max_length=1000, primary_key=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value[:30]