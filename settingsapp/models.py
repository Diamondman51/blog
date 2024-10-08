from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'About'

class Social_links(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(unique=True)

    class Meta:
        verbose_name_plural = "Social_links"

    def __str__(self):
        return self.name