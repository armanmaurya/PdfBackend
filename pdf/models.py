from django.db import models

# Create your models here.
class PDF(models.Model):
    name = models.CharField(max_length=300)
    file = models.FileField(upload_to="files")
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    