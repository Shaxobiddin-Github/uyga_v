from django.contrib import admin
from .models import News, Category,Tags,Comment
from django.utils.safestring import mark_safe
from django import forms
from ckeditor.widgets import CKEditorWidget


# Register your models here.




@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name',)
    search_fields = ('name',)
   

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)



class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('user', 'news', 'text', 'created')



class NewsAdminForm(forms.ModelForm):
    deskription = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = News
        fields = '__all__'

    
    
@admin.register(News)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at','get_image','videos')
    list_display_links = ('category',)
    search_fields = ('name', 'category',)
    list_editable = ('name',)


    def get_image(self,news):
        if news.image:
            return mark_safe(f'<img src="{news.image.url}" width ="75">')
        else:
            return mark_safe(f'<img src="https://demofree.sirv.com/nope-not-here.jpg" width ="75">')
    get_image.short_description = 'Rasmi'

    prepopulated_fields = {"slug":("name",)}