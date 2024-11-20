from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # عنوان کتاب
    author = models.CharField(max_length=100)  # نویسنده
    publication_date = models.DateField()  # تاریخ انتشار
    price = models.DecimalField(max_digits=10, decimal_places=2)  # قیمت

    def __str__(self):
        return self.title  # نمایش عنوان کتاب در پنل ادمین
