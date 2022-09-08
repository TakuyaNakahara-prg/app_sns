from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name = 'ユーザー')
    text = models.TextField(verbose_name = '本文')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = '投稿日時')

    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.TextField(verbose_name = 'コメント')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = '返信日時')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name = '大正の投稿')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'ユーザー')

    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'ユーザー'),
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name = '投稿'),
