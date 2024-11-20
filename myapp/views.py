from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

def book_list(request):
    books = Book.objects.all()  # تمام کتاب‌ها را از مدل دریافت کنید
    return render(request, 'book_list.html', {'books': books})



def home(request):
    return HttpResponse("Welcome to the Home Page!")
