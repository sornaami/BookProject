from django.db import models

# Create your models here.
class Book(models.Model):
    bookname=models.CharField(max_length=120,unique=True)
    price=models.IntegerField()
    pages=models.IntegerField()
    author=models.CharField(max_length=120)

    def __str__(self):
        return self.bookname
