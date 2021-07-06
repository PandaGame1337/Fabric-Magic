from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=225, verbose_name='Категория')
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
        

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=225, verbose_name='Название')
    slug = models.SlugField(unique=True)
    article = models.CharField(max_length=225, verbose_name='Артикул')
    photo = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
class Customers(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=225, verbose_name='Фамилия')
    first_name = models.CharField(max_length=225, verbose_name='Имя')
    middle_name = models.CharField(max_length=225, verbose_name='Отчество')
    email = models.CharField(max_length=225, unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=225, unique=True, verbose_name='Номер телефона')
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
                                  
    
