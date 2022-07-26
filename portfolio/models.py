from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    dascription = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/', height_field=None, width_field=None)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
