# Register your models here.
from django.contrib import admin  # 导入admin
from myblog import models  # 导入数据模型


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'timestamp')  # 设置要显示的属性，pk为索引。


admin.site.register(models.BlogPost, BlogPostAdmin)  # 使用admin注册BlogPostAdmin类