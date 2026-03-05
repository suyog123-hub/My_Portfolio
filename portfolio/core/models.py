from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True)
    subject=models.CharField(max_length=200,null=True)
    message=models.TextField(null=True)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=200,null=True)

class Project_title(models.Model):
    title=models.CharField(max_length=50,null=True)
    

    def __str__(self):
        return self.title
    
class Project_items(models.Model):

    category=models.ForeignKey(Project_title,on_delete=models.CASCADE,null=True)
    url = models.URLField(max_length=500,help_text="Enter the complete URL (e.g., https://example.com)",null=True)
    image=models.ImageField(upload_to="project items",null=True)
    heading=models.CharField(max_length=100,null=True)
    desc=models.TextField(null=True)
    language_used=models.CharField(max_length=100,null=True)


    
    
class skill_title(models.Model):
    title=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    
class skill_items(models.Model):
    category=models.ForeignKey(skill_title,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="skilll items",null=True)
    heading=models.CharField(max_length=100,null=True)
    desc=models.TextField(null=True)
    language_used=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

class Testinomial(models.Model):
    name=models.CharField(max_length=200,null=True)
    role=models.CharField(max_length=200,null=True)
    company=models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    feedback=models.TextField(null=True)
    image=models.ImageField(upload_to="testinomial_image",null=True)
    is_active=models.BooleanField(default=True)


class Skill(models.Model):
    icon=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    desc=models.TextField(null=True)
    percent=models.IntegerField(null=True)
    certificate=models.ImageField(upload_to='skill certficate',null=True,blank=True)
    # progress=models.CharField(max_length=100,null=True)

class Skill_tools(models.Model):
    icon=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)


    # class class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames'
    #     unique_together = (('date', 'table'),)