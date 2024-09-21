from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"  


class Tags(models.Model):
    name = models.CharField(max_length=30,verbose_name="Tag nomi")

    def __str__(self) -> str:
        return self.name     

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Taglar"



class News(models.Model):
    name = models.CharField(max_length=250,verbose_name = "Nomi")
    slug = models.SlugField(max_length=250,verbose_name ="Slug" )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name = "Kategoriya")
    deskription = models.TextField(blank=True,null=True,verbose_name = "Matni")
    image = models.ImageField( blank=True, null=True,verbose_name = "Rasmi")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = "Qushilgan vaqti")
    videos = models.FileField( blank=True, null=True,verbose_name = "Videosi")
    views = models.IntegerField(default=0, verbose_name="Kurishlar soni")
    is_active = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    is_banner = models.BooleanField(default=False, verbose_name="Bannerga chiqarish")
    is_weekly = models.BooleanField(default=False, verbose_name="Haftalik yangilk")
    tag = models.ManyToManyField(Tags, verbose_name="Taglar")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"  

 

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.text[:50]}..."