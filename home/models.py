from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    title = models.CharField(max_length=222)
    keywords = models.CharField(max_length=222)
    description = models.TextField(max_length=255)
    company = models.CharField(max_length=150)
    address=models.CharField(max_length=155, blank=True)
    phone = models.CharField(max_length=155, blank=True)
    fax = models.CharField(max_length=155, blank=True)
    email = models.CharField(max_length=155, blank=True)
    icon = models.ImageField(upload_to='images/', blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    twitter = models.CharField(max_length=155, blank=True)
    youtube = models.CharField(max_length=155, blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
       # ordering = ('name',)
        verbose_name = 'setting'
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class License(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = RichTextUploadingField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'
class Images(models.Model):
    product=models.ForeignKey(License, on_delete=models.CASCADE)
    title=models.CharField(max_length=50, blank=True)
    image=models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('Yangi', 'Yangi'),
        ("O'qildi", "O'qildi"),
        ('Yopilgan', 'Yopilgam')
    )
    name = models.CharField(blank=True,max_length=222)
    email = models.CharField(blank=True,max_length=222)
    subject = models.TextField(blank=True,max_length=255)
    message = models.TextField(blank=True, max_length=255)
    status=models.CharField(max_length=10, default='Yangi', choices=STATUS)
    ip = models.CharField(max_length=155, blank=True)
    note = models.CharField(max_length=155, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class':'input','placeholder':'Name'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message',
                                        'rows':'5'}),
        }