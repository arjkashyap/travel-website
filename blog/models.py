from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 150)
    body = models.TextField()
    date = models.DateTimeField()
    img_1 = models.FileField()
    img_2 = models.FileField()
    img_caption = models.TextField(default = "Image Caption")
    footer = models.TextField(default = "Summarize/Conclude")

    def  __str__(self):
        return self.title

