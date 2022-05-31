from django.db import models

# Create your models here.
CAT_CHOICES = (('C', 'Cricket'),('F','Football'))

class Blog(models.Model):
    category = models.CharField(choices=CAT_CHOICES, max_length=20)
    headline = models.TextField(max_length=70, null=False, blank=False)
    img = models.ImageField(upload_to="blog_imgs", null=True)
    start = models.TextField(max_length=10000)
    text = models.TextField(max_length=10000)
    date = models.DateField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
        return str(self.headline)