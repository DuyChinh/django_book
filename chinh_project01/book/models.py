from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)  # Thêm link ảnh
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
