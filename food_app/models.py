from django.db import models

# Create your models here.
# a model for storeing a food that can be ordered
class Food_Item(models.Model):
    def __str__(self) -> str:
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_type =  models.CharField(max_length=40)
    item_image = models.URLField(default='')



