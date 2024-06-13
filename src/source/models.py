from django.db import models


class Book(models.Model):

    book_id: str = models.CharField(max_length=9, primary_key=True)

    title: str = models.CharField(max_length=50)

    author: str = models.CharField(max_length=25)

    is_borrowed: bool = False

    is_expired: bool = False


class Member(models.Model):
    
    member_id: str = models.CharField(max_length=9, primary_key=True)

    name: str = models.CharField(max_length=25)

    borrowed_books: list[Book] = []
