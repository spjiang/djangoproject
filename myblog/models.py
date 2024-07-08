from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)  # 博客的标题
    body = models.TextField()  # 博客正文
    timestamp = models.DateTimeField()  # 博客创建时间

    class Meta:
        ordering = ('-timestamp',)