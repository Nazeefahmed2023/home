from django.db import models


# Create your models here.
class contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    phonenumber=models.IntegerField()

    def __str__(self):
        return super().__str__()
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/images',default="")
    def __str__(self):
        return self.product_name .__str__()


class Orders(models.Model):
    items_json=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    email=models.CharField(max_length=50)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=10)
    zip_code=models.IntegerField(max_length=10)
    oid=models.CharField(max_length=50,blank=True)
    amountpaid=models.CharField(max_length=50,blank=True,null=True)
    paymentstatus=models.CharField(max_length=20,default="")
    phone=models.CharField(max_length=100,default="")
    

    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.update_desc[0:7] + "..."
