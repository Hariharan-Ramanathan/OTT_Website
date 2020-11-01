from django.db import models

class thumbnail(models.Model):
    #id = model.AutoField(primary_key=True)
    image = models.FileField(upload_to = "image/", blank=True, null=True)
    content = models.TextField(blank=True, null=True)