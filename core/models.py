from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name or 'Contact'} - {self.subject or 'No subject'}"

class Project_title(models.Model):
    title=models.CharField(max_length=50,null=True,blank=True)
    

    def __str__(self):
        return self.title or f"Category #{self.pk}"
    
class Project_items(models.Model):

    STATUS_CHOICES = [
        ('DELIVERED', 'Delivered'),
        ('ONGOING', 'Ongoing'),
        ('REFINING', 'Refining'),
        ('LIVE', 'Live'),
    ]

    category = models.ForeignKey(Project_title, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(max_length=500, help_text="Enter the complete URL (e.g., https://example.com)", null=True, blank=True)
    github_url = models.URLField(max_length=500, help_text="GitHub repository URL (optional — hides the Code button when empty)", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DELIVERED')
    image = models.ImageField(upload_to="project_items/", null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    language_used = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.heading or f"Project #{self.pk}"


    
    
class skill_title(models.Model):
    title=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title or f"Skill group #{self.pk}"
    
    
class skill_items(models.Model):
    category = models.ForeignKey(skill_title, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="skill_items/", null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    language_used = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.heading or f"Skill item #{self.pk}"

class Testinomial(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="testinomial_image/", null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name or 'Anonymous'} - {self.company or 'No company'}"


class Skill(models.Model):
    icon = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    percent = models.IntegerField(null=True, blank=True)
    certificate = models.ImageField(upload_to='skill_certificates/', null=True, blank=True)
    # progress=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name or f"Skill #{self.pk}"

class Skill_tools(models.Model):
    icon = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name or f"Tool #{self.pk}"


    # class class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames'
    #     unique_together = (('date', 'table'),)

