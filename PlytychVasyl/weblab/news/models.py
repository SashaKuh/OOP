from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва тексту:', max_length=100)
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Головний текс')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title