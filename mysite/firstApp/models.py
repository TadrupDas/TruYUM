from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    name=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    active=models.BooleanField()
    launch_date=models.DateField()
    category=models.CharField(max_length=250)
    free_delivery=models.BooleanField()
    date_created=models.DateTimeField()

def __repr__(self) -> str:
        return f"{self.id} - {self.name} - {self.price} - {self.active} - {self.launch_date} - {self.category} - {self.free_delivery} - {self.date_created}"

#Cart Item Models
class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category_type = models.CharField(max_length=250)
    delivery_free = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __repr__(self) -> str:
        return f"{self.id} - {self.user_id} - {self.name} - {self.price} - {self.delivery_free} - {self.category_type} - {self.date_created}"