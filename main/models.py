from django.db import models

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"  

class News(models.Model):
    name = models.CharField(max_length=250,verbose_name = "Nomi")
    slug = models.SlugField(max_length=250,verbose_name ="Slug" )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name = "Kategoriya")
    deskription = models.TextField(blank=True,null=True,verbose_name = "Matni")
    image = models.ImageField( blank=True, null=True,verbose_name = "Rasmi")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = "Qushilgan vaqti")
    videos = models.FileField( blank=True, null=True,verbose_name = "Videosi")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"  