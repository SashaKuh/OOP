from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    anons = models.CharField('Anons', max_length=100)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.title