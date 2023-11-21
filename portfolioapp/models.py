from django.db import models
import datetime

# Create your models here.
class Aboutme(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    Birthday=models.DateField(default=datetime.datetime.today)
    profile_pic = models.ImageField(upload_to='Uploaded/Profile_pic/')
    short_description = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    linkdin = models.URLField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    freelance_status = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta:        
        verbose_name = 'Aboutme'
        verbose_name_plural = 'Aboutmes'
#############################################

class Count(models.Model):
    what_count = models.CharField(max_length=100, blank=True, null=True)
    count_number = models.IntegerField(blank=True, null=True)
    icon =  models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.what_count
    
    class Meta:
        verbose_name = 'Count'
        verbose_name_plural = 'Counts'

############################################

class Skill(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    progress = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

##############################################

class Interest(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    icon =  models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:        
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'

##############################

class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'