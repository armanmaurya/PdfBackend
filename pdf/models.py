from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class PDF(models.Model):
    name = models.CharField(max_length=300)
    file = models.FileField(upload_to="files")
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    



    