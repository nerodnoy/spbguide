from django.db import models
from django.urls import reverse


class Restaurants(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Посл. изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    # _id будет добавлено в имя автоматически Джангой
    # null=True временно заполнит новые поля нулями. Это нужно при makemigrations
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    # Здесь создаём ссылку для объекта
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Популярные рестораны'
        verbose_name_plural = 'Популярные рестораны'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    # Благодаря этой функции админ-панель демонстрирует ссылку на ресторан
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
