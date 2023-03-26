from django.db import models
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    tags=models.TextField()
    img=models.FileField(upload_to="pic/%y/")
    img2 = models.FileField(upload_to="pict/%y/")
    img3 = models.FileField(upload_to="pictu/%y/")
    img4 = models.FileField(upload_to="pictur/%y/")
    desc = models.CharField(max_length=300)
    descc = models.CharField(max_length=1800)
    desccc = models.CharField(max_length=3000)

    def __str__(self):
        return self.title
    class Meta  :
        ordering=('-id',)

    def get_absolute_url(self):
        return reverse('details',args=[self.id,self.slug])
