from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from app01.models import Publisher, Book, Author
from app01 import models
from django.views import View
from django.urls import reverse
from functools import wraps
from django.utils.decorators import method_decorator  # 类的方法装饰器.
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def login_require(func):
    @wraps(func) # 装饰器函数修复.
    def inner(requests, *args, **kwargs):
        url_prev = requests.path_info
        # login_flag = requests.COOKIES.get("is_login", None)
        login_flag = requests.session.get("is_login", None)
        if login_flag == "1":
            ret = func(requests, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(url_prev))
        return ret
    return inner

# Create your views here.
@login_require
def publisher_list(requests):
    data = Publisher.objects.all().order_by("id")
    return render(requests, "list_publisher_02.html", {"publisher_list": data})


# def delete_publisher(requests):
#     del_id = requests.GET.get("id", None)
#     obj = Publisher.objects.filter(id=del_id)
#     obj.delete()
#     return redirect("/publisher_list/")

# URL 分组传参.
def delete_publisher(requests, d_id):
    obj = Publisher.objects.get(id=d_id)
    obj.delete()
    return redirect("/publisher_list/")

def add_publisher(requests):
    if requests.method == 'POST':
        name = requests.POST.get("publisher_name", None)
        obj = Publisher.objects.create(name=name)
        return redirect("/publisher_list/")
    return render(requests, "add_publisher.html")


class AddPublisher(View):
    @method_decorator(login_require)  # 类中方法装饰器.
    def get(self, requests):
        return render(requests, "add_publisher.html")

    def post(self, requests):
        name = requests.POST.get("publisher_name", None)
        obj = Publisher.objects.create(name=name)
        return redirect("/publisher_list/")


def edit_publisher(requests):
    if requests.method == "POST":
        publisher_id = requests.POST.get("publisher_id", None)
        publisher_name = requests.POST.get("publisher_name", None)
        publisher_obj = Publisher.objects.get(id=publisher_id)
        publisher_obj.name = publisher_name
        publisher_obj.save()
        return redirect("/publisher_list/")
    publisher_id = requests.GET.get("id")
    # publisher_obj = Publisher.objects.get(id=publisher_id)
    publisher_obj = get_object_or_404(Publisher, id=publisher_id)
    return render(requests, "edit_publisher.html", {"publisher_obj": publisher_obj})

@login_require
def list_book(requests):
    page_num = requests.GET.get("page", 1)
    # 输入异常情况自动跳转第一页.
    try:
        page_num = int(page_num)
    except Exception:
        page_num = 1
    # 获取总页数.
    total_num = Book.objects.all().count()
    pn, mod = divmod(total_num, 10)
    if mod>0:
        pn += 1
    # 每页多少个分页处理.
    max_per_page = 11
    half_max_per_page = max_per_page//2
    if page_num <= half_max_per_page:
        start_page = 1
        end_page = 11
    else:
        start_page = page_num - half_max_per_page
        end_page = page_num + half_max_per_page + 1

    start_ele = (page_num - 1) * 10
    end_ele = page_num * 10
    data = Book.objects.all()[start_ele:end_ele]
    li = []
    for i in range(start_page, end_page):
        if i == page_num:
            li.append('<li class="active"><a href="/?page={0}">{0}</a></li>'.format(i))
        else:
            li.append('<li><a href="/?page={0}">{0}</a></li>'.format(i))
    li_html = "".join(li)
    return render(requests, "list_book_02.html", {"book_list": data, "li_html": li_html, "pn": pn})


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

@login_require
def list_author(requests):
    data = Author.objects.all().order_by("id")
    return render(requests, "list_author_02.html", {"list_author": data})


def delete_author(requests):
    del_id = requests.GET.get("id")
    author_obj = Author.objects.get(id=del_id)
    author_obj.delete()
    return redirect("/list_author/")

def delete_action(requests, table_name, row_id):
    if hasattr(models, table_name):
        table_obj = getattr(models, table_name)
        print(table_obj)
        table_obj.objects.get(id=row_id).delete()
        return redirect("/list_author/")
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
    url_index = reverse("index")
    print(url_index)
    response = JsonResponse({"name": "lance"})
    response.setdefault("Access-Control-Allow-Origin", "*")
    return response


class upload_file(View):

    def get(self, requests):
        return render(requests, "upload_file.html")

    def post(self, requests):
        file_obj = requests.FILES.get("file_name")
        with open(file_obj.name, 'wb') as fd:
            for chunk in file_obj.chunks():
                fd.write(chunk)
        return HttpResponse("upload done.")

@csrf_protect  # 给指定函数加上CSRF_Token校验.
def login(requests):
    if requests.method == "POST":
        username = requests.POST.get("username", None)
        password = requests.POST.get("password", None)
        next_url = requests.GET.get("next", "/")
        requests.session["is_login"] = "1" # 设置Session. session对象保存在requests对象中.
        if username == "lance" and password == "password":
            response = redirect(next_url)
            # response.set_cookie("is_login", "1") # 设置Cookie.
            return response
        return redirect(reverse("login"))
    return render(requests, "login.html")

def logout(requests):
    requests.session.flush() # 清除Session以及数据库中存储的数据.
    return redirect(reverse("login"))


def ajax_html(requests):
    return render(requests, "ajax_html.html")


def ajax_get(requests):
    i1 = requests.GET.get("i1", 0)
    i2 = requests.GET.get("i2", 0)
    i3 = int(i1) + int(i2)
    response = HttpResponse(i3)
    response.setdefault("Access-Control-Allow-Origin", "*") # 解决跨域问题.
    return response

def ajax_post(requests):
    i1 = requests.POST.get("i1", 0)
    i2 = requests.POST.get("i2", 0)
    i3 = int(i1) + int(i2)
    response = HttpResponse(i3)
    response.setdefault("Access-Control-Allow-Origin", "*") # 解决跨域问题.
    return response
