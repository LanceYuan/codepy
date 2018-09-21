from django.contrib import admin
from app01.models import Book, Author, Publisher, AuthorDetail
from django.utils.safestring import mark_safe
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    def delete_action(self): # 自定义字段.
        return mark_safe("<a href="">delete</a>")

    list_display = ["id", "name", "price", "publisher", "create_time", "modify_time", delete_action]
    list_display_links = ["name"] # 关联修改连接的字段.
    list_filter = ["publisher", "price"]
    search_fields = ["name"]
    # 后台批量改价操作
    def patch_init(self, request, queryset):
        queryset.update(price=9.9)
    patch_init.short_description = "批量改价"
    actions = [patch_init, ]
    # 修改模板文件.
    # change_list_template = "list_book_02.html"

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(AuthorDetail)
