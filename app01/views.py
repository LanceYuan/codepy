from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from app01.models import Publisher, Book, Author, Userinfo
from app01 import models
from django.views import View
from django.urls import reverse
from functools import wraps
from django.utils.decorators import method_decorator  # 类的方法装饰器.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from django import forms
from django.forms import widgets
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


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


# @login_required
def index(requests):
    url_index = reverse("index")
    print(url_index)
    response = JsonResponse({"name": "lance"})
    return response


class upload_file(View):
    @method_decorator(login_required)
    def get(self, requests):
        user = requests.user
        return render(requests, "upload_file.html", {"user": user})

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


@csrf_protect
def ajax_post(requests):
    i1 = requests.POST.get("i1", 0)
    i2 = requests.POST.get("i2", 0)
    i3 = int(i1) + int(i2)
    response = HttpResponse(i3)
    response.setdefault("Access-Control-Allow-Origin", "*") # 解决跨域问题.
    return response


from rest_framework import serializers as rest_serializers
from rest_framework.views import APIView
from rest_framework.response import Response
class PublisherSerializer(rest_serializers.Serializer):
    id = rest_serializers.IntegerField()
    name = rest_serializers.CharField()


class BookSerializer(rest_serializers.Serializer):
    id = rest_serializers.IntegerField()
    name = rest_serializers.CharField()
    price = rest_serializers.FloatField()
    publisher = PublisherSerializer() # 外键字段.
    # publisher = rest_serializers.CharField(source="publisher.name")


class AuthorSerializer(rest_serializers.Serializer):
    id = rest_serializers.IntegerField()
    name = rest_serializers.CharField()
    book = rest_serializers.SerializerMethodField() # 多对多的时候使用SerializerMethodField

    def get_book(self, obj):            # 当前obj为book对象.
        book_list = []
        for book_obj in obj.book.all(): # 获取当前book对象所有书籍.
            book_list.append(book_obj.name)
        return book_list                # 代表序列化中book字段的数据.


class BookModelSerializer(rest_serializers.ModelSerializer):
    # publisher = rest_serializers.CharField(source="publisher.name")
    class Meta:
        model = Book       # models中类名
        fields = "__all__" # 需要的字段.
    def create(self, validated_data):  # 保存失败，需要重写create方法.
        print(validated_data)
        data = {}
        data["name"] = validated_data["name"]
        data["publisher_id"] = validated_data["publisher"]["name"]
        data["price"] = validated_data["price"]
        book_obj = Book.objects.create(**data)
        return book_obj
    def update(self, obj, validated_data):  # 保存失败，需要重写update方法.
        obj.name = validated_data["name"]
        obj.publisher = validated_data["publisher"]  # 这个一个Publisher对象.
        obj.price = validated_data["price"]
        obj.save()
        return obj


class RestSerial(APIView):
    @method_decorator(login_required)
    @method_decorator(permission_required("admin.add_logentry"))
    def get(self, requests):
        data = Book.objects.all()
        # s_data = BookSerializer(data, many=True)      # BookSerializer生成OrderedDict对象.
        s_data = BookModelSerializer(data, many=True)   # BookModelSerializer生成OrderedDict对象.
        return Response(s_data.data)                    # 使用rest_framework生成向应数据.
        # return JsonResponse(s_data.data, safe=False)  # JsonResponse非字典对像需要加上safe=False
    def post(self, requests):
        data_obj = BookModelSerializer(data=requests.data)
        if data_obj.is_valid():
            data_obj.save()         # save方法实际会执行类的Create方法.
            return Response(data_obj.data)
        else:
            return Response(data_obj.errors)

class RestSerialDetail(APIView):
    def put(self, requests, pid):
        book_obj = Book.objects.get(pk=pid)
        s_data = BookModelSerializer(book_obj, data=requests.data)
        if s_data.is_valid():
            s_data.save()
            return Response(s_data.data)
        else:
            return Response(s_data.errors)
    def delete(self, requests, pid):
        book_obj = Book.objects.get(pk=pid)
        book_obj.delete()
        return Response("")


class AuthSerial(APIView):
    def get(self, requests):
        book_list = Author.objects.all()
        s_data = AuthorSerializer(book_list, many=True)
        return Response(s_data.data)


def serialization(requests):
    from django.core import serializers
    data = Book.objects.all()
    s_data = serializers.serialize("json", data)
    return HttpResponse(s_data)


def ajax_deletebook(requests):
    location_url = requests.POST.get("location_url")
    del_id = requests.POST.get("del_id")
    Book.objects.filter(id=del_id).delete()
    print(del_id)
    return HttpResponse(location_url)


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        min_length=8,
        label="用户名",
        required=True,
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={"required": "用户名不能为空", "min_length": "用户名不能小于8位"}
    )
    password = forms.CharField(
        max_length=64,
        min_length=8,
        label="密码",
        required=True,
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control"}),
        error_messages={"required": "密码不能为空"}
    )
    chkpwd = forms.CharField(
        max_length=64,
        min_length=8,
        label="确认密码",
        required=True,
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control"}),
        error_messages={"required": "确认密码不能为空"}
    )
    gender = forms.ChoiceField(
        choices=((1, "男"), (0, "女")),
        initial=1,
        label="性别",
        widget=forms.widgets.RadioSelect()
    )
    email = forms.CharField(
        max_length=32,
        label="邮箱",
        required=False,
        widget=forms.widgets.EmailInput(attrs={"class": "form-control"})
    )
    avatar = forms.FileField(
        label="图像",
        widget=forms.widgets.FileInput()
    )


def register(requests):
    if requests.method == "POST":
        form_obj = RegForm(requests.POST, requests.FILES)
        if form_obj.is_valid():
            data = form_obj.cleaned_data
            if data["password"] == data["chkpwd"]:
                data.pop("chkpwd")
                Userinfo.objects.create(**data)
                return HttpResponse("register success.")
            else:
                return HttpResponse("register failure.")
        else:
            # return render(requests, "register.html", {"form_obj": form_obj})
            response = {"msg": form_obj.errors}
            return JsonResponse(response)
    form_obj = RegForm()
    return render(requests, "register.html", {"form_obj": form_obj})


def auth_login(requests):
    prev_url = requests.GET.get("next", "/upload/")
    if requests.method == "POST":
        username = requests.POST.get("username")
        password = requests.POST.get("password")
        # 判断用户名密码是否正确.
        user = auth.authenticate(username=username, password=password)
        if user:
            # 在requests对象中添加user属性.
            auth.login(requests, user)
            return redirect(prev_url)
    return render(requests, "auth_login.html", {"prev_url": prev_url})


def auth_reg(requests):
    if requests.method == "POST":
        username = requests.POST.get("username")
        password = requests.POST.get("password")
        chkpwd = requests.POST.get("chkpwd")
        email = requests.POST.get("email")
        user_obj = User.objects.filter(username=username)
        if (not user_obj) and password == chkpwd:
            user_obj = User.objects.create_user(username=username, password=password, email=email)
            user_obj.save()
            # 注册完并登陆
            auth.login(requests, user_obj)
            return redirect("/upload/")
    return render(requests, "auth_reg.html")


def auth_logout(requests):
    auth.logout(requests)
    return redirect("/auth_login/")


def kind_upload(requests):
    from django.conf import settings
    file_obj = requests.FILES.get("imgFile")
    with open("{0}/upload/{1}".format(settings.MEDIA_ROOT, file_obj.name), "wb") as fd:
        for chunk in file_obj.chunks():
            fd.write(chunk)
    response = {"error": 0, "url": "{0}/upload/{1}".format(settings.MEDIA_URL, file_obj.name)}
    return JsonResponse(response)
