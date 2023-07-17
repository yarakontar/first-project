from django.db import models



# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=4)
    
    def __str__(self):
        return self.name
    

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    status = models.CharField(max_length=255, choices=[
        ('IN_PROGRESS', 'جاري الانتظار'),
        ('COMPLETED', 'تمت'),
        ('FAILED', 'فشلت'),
    ])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.total_amount} -  {self.status}-{self.created_at}'
