from django.db import models

# Create Product database
class Items(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50,default="Enter Your Name")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/image',default="")


#ye line likhne se admin k database me jo product ka name h ussi se uss product ki sari database ki value show hogi
    def __str__(self):
        return self.product_name


# Database of Contact Page

class Contacts(models.Model):
    contact_id = models.AutoField
    Name = models.CharField(max_length=50,default="Name")
    Email = models.CharField(max_length=50, default="Email")
    Phone = models.IntegerField(default="Phone Number")
    desc = models.CharField(max_length=300,default="Enter Your Khawaish")

    def __str__(self):
        return self.Name

class Checkout(models.Model):
    OrderId = models.CharField(max_length=100, default="Order Id")
    Product = models.CharField(max_length=1000, default="product name")
    Name = models.CharField(max_length=50, default="Name")
    Email = models.CharField(max_length=50, default="Email")
    Address = models.CharField(max_length=50, default="Address")
    City = models.CharField(max_length=50, default="City")
    State = models.CharField(max_length=50, default="State")
    Pincode = models.IntegerField(default="Pincode")
    Phone = models.CharField(max_length=11,default="Phone Number")

    def __str__(self):
        return self.Name

class Tracker(models.Model):
    OrderId = models.CharField(max_length=100, default="Order Id")
    Description = models.CharField(max_length=500,default="Enter Aboout Product")
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.OrderId
