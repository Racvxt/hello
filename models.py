from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=20)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
class Destination(models.Model):
    username=models.CharField(max_length=10)
    firstname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

