import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codepy.settings")
    import django
    django.setup()
    from app01.models import Book, Publisher, Author, AuthorDetail, Userinfo

    # 查询所有的书籍.
    books = Book.objects.all()
    # print(books)
    book_one = Book.objects.get(id=3)
    book_two = Book.objects.get(name="Python全栈S10")
    # 查询ID大于1且小于10的书籍.
    book_three = Book.objects.filter(id__gt=1, id__lt=10)
    # 返回QuerySet指定字段的字典形式. 默认返回所有字段.
    book_info = Book.objects.values("name", "create_time")
    # 返回指定字段的元组形式. 没有字段名称。
    book_list = Book.objects.values_list("name", "create_time")
    # 按照指定字段的排序(升序).
    book_order_1 = Book.objects.all().order_by("modify_time")
    # 排序后反转.
    book_order_2 = Book.objects.all().order_by("modify_time").reverse()
    # 降序.
    book_order_3 = Book.objects.all().order_by("-modify_time")
    # 返回QuerySet对象数量.
    book_count = Book.objects.all().count()
    # 返回QuerySet第1个数据.
    book_first = Book.objects.all().first()
    # 返回QuerySet最后1个数据.
    book_last = Book.objects.all().last()
    # 数据是否存在.
    book_exist = Book.objects.filter(id=1000).exists()
    # 查询ID 在[1, 3, 5, 7, 9]里面的数据.
    book_in = Book.objects.filter(id__in=[1, 3, 5, 7, 9])
    # not in
    book_not_in = Book.objects.exclude(id__in=[1, 3, 5, 7])
    # name包含指定字符的数据.
    book_contains = Book.objects.filter(name__contains="Java")
    book_i_contains = Book.objects.filter(name__icontains="java")
    # 查询ID在指定区间，类似SQL的 BETWEEN AND.
    book_between = Book.objects.filter(id__range=[1, 5])
    # 根据日期指定哪天来过滤.
    book_date = Book.objects.filter(modify_time__day=6)
    # 外键的跨表查询.
    # 正向查找，查询ID为3的书籍对应的出版社.
    book_publisher = Book.objects.get(id=3).publisher
    book_publisher_name_1 = Book.objects.get(id=3).publisher.name
    # 查询ID为3的书籍对应的出版社名称.使用__方法
    book_publisher_name_2 = Book.objects.filter(id=3).values("publisher__name")
    # 查询出版社名称为上海老男孩出版社的书籍.
    book_publisher_name_3 = Book.objects.filter(publisher__name="上海老男孩出版社")
    # 反向查找，查询出版社对应的书籍. publisher_obj.表名_set
    publisher_obj = Publisher.objects.get(id=6)
    publisher_obj_book = publisher_obj.book_set.all()
    # 基于双下划线的查询.
    publisher_books = Publisher.objects.filter(id=6).values("book__name")
    # 多对多增删改查.
    author_obj = Author.objects.first()
    author_obj_books = author_obj.book.all()
    # 根据Author_obj创建书籍并关联作者和出版社，并且返回的是书的对象.
    # auth_create_book = author_obj.book.create(name="Django 开发", publisher_id=6)
    # 给author_obj对象新增一本书,在原有数据的基础上增加.
    # author_obj.book.add(id=6)
    # author_obj.book.add(11, 12)
    # books = Book.objects.filter(id__gt=10)
    # author_obj.book.add(*books)
    # 给Author_obj设置新的books,所有ID大于10的书籍，原有的数据会删除.
    # books = Book.objects.filter(id__gt=10)
    # author_obj.book.set(books)
    # 给Author_obj 删除指定书籍.
    # book_del = Book.objects.get(id=11)
    # author_obj.book.remove(book_del)
    # 清空author_obj关联的所有书籍. 注意数据库中表字段是否能为空.
    # author_obj.book.clear()
    # 聚合函数.
    from django.db.models import Avg, Sum, Max, Min, Count
    price_avg = Book.objects.all().aggregate(Avg("price"))
    price_sum = Book.objects.all().aggregate(Sum("price"))
    price_max = Book.objects.all().aggregate(Max("price"))
    # price_min指定返回数据的KEY.
    price_min = Book.objects.all().aggregate(price_min=Min("price"))
    price_all = Book.objects.all().aggregate(price_min=Min("price"), price_max=Max("price"), price_avg=Avg("price"))
    # 分组. 查询所有书籍关联的作者数量，Count后面直接跟表名.
    books_obj = Book.objects.all().annotate(author_num=Count("author"))
    for item in books_obj:
        print(item.name, item.author_num)
    # 所有书籍作者大于1的数据.
    books_obj = Book.objects.all().annotate(author_num=Count("author")).filter(author_num__gt=1)
    # F 和 Q 查询.
    from django.db.models import F, Q
    # F 查询，查询所有修改时间大于创建时间的数据.
    book_obj = Book.objects.filter(modify_time__gt=F("create_time"))
    # 通过F查询修改原有数据. 所有书的价格乘以2
    # Book.objects.update(price=F("price")*2)
    # Q 查询，多个条件之间的或操作.
    book_q_obj = Book.objects.filter(Q(id__gt=11) | Q(price__lt=200))
    # 一对一关关联.
    # 通过author_obj查找祥细信息.
    author_obj = Author.objects.first()
    author_detail_lang = author_obj.detail.language
    # 通过author_detail反向查找Author信息。  对象后面直接跟表名字段名称.
    author_detail_obj = AuthorDetail.objects.first()
    author_detail_name = author_detail_obj.author.name
    # 分组+聚合查询.
    # 以publisher_id进行分组.聚合算平均值.获取出版社书籍的平均价.
    books_obj = Book.objects.values("publisher_id").annotate(price_avg=Avg("price")).values("publisher__name", "price_avg")

    # 文件对象.
    user_obj = Userinfo.objects.first()

    # Django中执行原生的SQL.
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select * from app01_book where id > %s", (10,))
    data = cursor.fetchall()
    print(data)
