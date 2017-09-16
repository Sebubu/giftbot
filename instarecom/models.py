from django.db import models

# Create your models here.
class RecommendRequest(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    targetUser = models.CharField(max_length=50)
    productList = models.TextField()

    @property
    def is_finished(self):
        return self.productList != ''
