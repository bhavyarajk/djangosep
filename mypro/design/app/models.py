from django.db import models

class place(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    img=models.ImageField(upload_to='places')

