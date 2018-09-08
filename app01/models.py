from django.db import models

# Create your models here.

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Publisher object: {0}>".format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to="Publisher") # related_name用于Publisher反向查找时使用，publisher.books.all()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Book object: {0}>".format(self.name)

    # 指定表的元数据.
    # class Meta:
        # db_table = "Book" # 表名
        # ordering = ("modify_time",) # 默认排序字段.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    book = models.ManyToManyField(to="Book")
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Author object: {0}>".format(self.name)
