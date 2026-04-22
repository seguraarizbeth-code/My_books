from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.CharField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title