from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50,default='Anonymous')
    age = models.IntegerField(null=True,blank=True)
    
    
    # def __str__(self):
    #     return self.name,


class BookCategory(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(max_length=10)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    price = models.IntegerField()
    category = models.ForeignKey(BookCategory,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    