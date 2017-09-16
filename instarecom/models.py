from django.db import models


class RecommendRequest(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    targetUser = models.CharField(max_length=50)
    productList = models.TextField()
    personality = models.TextField(default='')
    user_info = models.TextField(default='')

    @property
    def is_finished(self):
        return self.productList != ''
