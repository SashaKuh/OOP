# main/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])  # Рейтинг від 1 до 10
    release_date = models.DateField()  # Додайте поле для дати
    description = models.TextField()

    def __str__(self):
        return self.title
