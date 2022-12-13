from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DatabaseBlog(models.Model):
    blog_id = models.AutoField
    BlogTitle = models.CharField(max_length=30,default="Title")
    BlogDate = models.DateTimeField(auto_now_add=True)
    BlogMoral = models.CharField(max_length=50,default="Moral Of the Blog")
    BlogDetails = models.CharField(max_length=5000,default="Write Complete Blog")
    BlogAuthor = models.CharField(max_length=20,default="Name Of Blogger")
    BlogImage = models.ImageField(upload_to='shop/image', default=" ")

    def __str__(self):
        return self.BlogTitle

class PublishBlog(models.Model):
    publish_id= models.AutoField
    Author_Name = models.CharField(max_length=50)
    Blogger_Email = models.CharField(max_length=50)
    Blogger_Title = models.CharField(max_length=80)
    Blogger_Content = models.CharField(max_length=5000000)
    Blog_Image = models.ImageField(upload_to='shop/image/')
    Blog_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Blogger_Title

class Comments(models.Model):
    Sno = models.AutoField(primary_key = True)
    Product_Id = models.CharField(max_length=1000)
    Reply_id = models.IntegerField()   #this can store the parent comment Sno
    Comment = models.TextField(max_length=500)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Post = models.ForeignKey(DatabaseBlog,on_delete=models.CASCADE)
    Parent = models.ForeignKey('self',on_delete=models.CASCADE,null = True)
    Commment_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Comment[0:20]

class Publish_Comments(models.Model):
    Sno = models.AutoField(primary_key = True)
    Product_Id = models.CharField(max_length=1000)
    Reply_id = models.IntegerField()   #this can store the parent comment Sno
    Post_Comment_On_User_Blog = models.ForeignKey(PublishBlog, on_delete=models.CASCADE)
    Comment = models.TextField(max_length=500)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Parent = models.ForeignKey('self',on_delete=models.CASCADE,null = True)
    Commment_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Comment[0:20]
