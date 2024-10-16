from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва', max_length=100)
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Текст')
    data = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новини'
        verbose_name_plural = 'Новинии'