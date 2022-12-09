from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name


class Notebook(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='nout_category')
    name = models.CharField('Notebook name', max_length=50)
    price = models.IntegerField('Notebook price')
    img = models.ImageField('Notebook img', upload_to='media')

    def __str__(self):
        return self.name
        