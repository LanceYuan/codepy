import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codepy.settings")
    import django
    django.setup()
    from app01.models import Book, Publisher, Author

    # 查询所有的书籍.
    books = Book.objects.all()
    # print(books)
    book_one = Book.objects.get(id=3)
    book_two = Book.objects.get(name="战神")
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
    #
    print(publisher_books)
