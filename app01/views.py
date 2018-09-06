from django.shortcuts import render, redirect
from app01.models import Publisher, Book, Author

# Create your views here.
def publisher_list(requests):
    data = Publisher.objects.all().order_by("id")
    return render(requests, "list_publisher_02.html", {"publisher_list": data})

def delete_publisher(requests):
    del_id = requests.GET.get("id", None)
    obj = Publisher.objects.filter(id=del_id)
    obj.delete()
    return redirect("/publisher_list/")

def add_publisher(requests):
    if requests.method == 'POST':
        name = requests.POST.get("publisher_name", None)
        obj = Publisher.objects.create(name=name)
        return redirect("/publisher_list/")
    return render(requests, "add_publisher.html")

def edit_publisher(requests):
    if requests.method == "POST":
        publisher_id = requests.POST.get("publisher_id", None)
        publisher_name = requests.POST.get("publisher_name", None)
        publisher_obj = Publisher.objects.get(id=publisher_id)
        publisher_obj.name = publisher_name
        publisher_obj.save()
        return redirect("/publisher_list/")
    publisher_id = requests.GET.get("id")
    publisher_obj = Publisher.objects.get(id=publisher_id)
    return render(requests, "edit_publisher.html", {"publisher_obj": publisher_obj})


def list_book(requests):
    data = Book.objects.all()
    return render(requests, "list_book_02.html", {"book_list": data})


def add_book(requests):
    if requests.method == 'POST':
        book_name = requests.POST.get("book_name", None)
        publisher_id = requests.POST.get("publisher_id", None)
        obj = Book.objects.create(name=book_name, publisher_id=publisher_id)
        return redirect("/list_book/")
    publisher_list = Publisher.objects.all().order_by("id")
    return render(requests, "add_book.html", {"publisher_list": publisher_list})


def delete_book(requests):
    del_id = requests.GET.get("id", None)
    obj = Book.objects.get(id=del_id)
    obj.delete()
    return redirect("/list_book/")


def edit_book(requests):
    if requests.method == "POST":
        edit_id = requests.POST.get("book_id", None)
        book_name = requests.POST.get("book_name", None)
        publisher_id = requests.POST.get("publisher_name", None)
        book_obj = Book.objects.get(id=edit_id)
        book_obj.name = book_name
        book_obj.publisher_id = publisher_id
        book_obj.save()
        return redirect("/list_book/")
    edit_id = requests.GET.get("id")
    book_obj = Book.objects.get(id=edit_id)
    publisher_obj = Publisher.objects.all()
    return render(requests, "edit_book.html", {"book_obj": book_obj, "publisher_obj": publisher_obj})


def list_author(requests):
    data = Author.objects.all().order_by("id")
    return render(requests, "list_author_02.html", {"list_author": data})


def delete_author(requests):
    del_id = requests.GET.get("id")
    author_obj = Author.objects.get(id=del_id)
    author_obj.delete()
    return redirect("/list_author/")

def add_author(requests):
    if requests.method == "POST":
        author_name = requests.POST.get("author_name", None)
        book_list = requests.POST.getlist("books_name") # 获取多个值的时候使用.multiple, checkbox
        author_obj = Author.objects.create(name=author_name)
        author_obj.book.set(book_list) # 更新第3张表的数据.
        return redirect("/list_author/")
    books = Book.objects.all()
    return render(requests, "add_author.html", {"list_book": books})

def edit_author(requests):
    if requests.method == "POST":
        edit_id = requests.POST.get("author_id")
        author_name = requests.POST.get("author_name")
        book_list = requests.POST.getlist("books_name")
        edit_author_obj = Author.objects.get(id=edit_id)
        edit_author_obj.name = author_name
        edit_author_obj.book.set(book_list)
        edit_author_obj.save()
        return redirect("/list_author/")
    edit_id = requests.GET.get("id")
    edit_author_obj = Author.objects.get(id=edit_id)
    books = Book.objects.all()
    return render(requests, "edit_author.html", {"list_book": books, "author": edit_author_obj})

def t_filter(requests):
    import time, datetime
    # now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    now_time = datetime.datetime.now()
    script_html = '<script>alert("Hello World")</script>'
    script_safe = '<script>for(var i=1;i<4;i++){alert(i);}</script>'
    data = {
        "name": "lance",
        "age": 32,
        "script_str": script_html,
        "script_safe": script_safe,
        "now_time": now_time,
        "girl": "Lily"
    }
    return render(requests, "t_filter.html", data)


def index(requests):
    return render(requests, "base.html")