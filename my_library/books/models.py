from django.db import models

class Authors(models.Model):
    author_of_book =models.CharField(max_length=100)
    def __str__(self):
        return self.author_of_book

class Categories(models.Model):
    name_of_category =models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_category

class Books(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    description = models.TextField()
    categories = models.ManyToManyField('Categories', related_name='books')



