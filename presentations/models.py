from django.db import models

class Presentations(models.Model):
    image = models.ImageField(upload_to='images/', default='ptf/static/MIT-Earth-Dish_0.jpg')
    imagebody = models.ImageField(upload_to= 'images/', default='ptf/static/MIT-Earth-Dish_0.jpg')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
