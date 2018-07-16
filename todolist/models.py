# -- coding: utf-8 --
from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=50)      # 标题
    body = models.TextField()        # 任务的具体内容，正文
    complete = models.BooleanField(default=False)
    pri = models.IntegerField(default=1)     # 优先级 1，2，3，4
    expire_date = models.DateTimeField(auto_now=False, auto_now_add=True)

'''
auto_now
Automatically set the field to now every time the object is saved. Useful for "last-modified"
 timestamps. Note that the current date is always used; it's not just a default value that you
 can override.

auto_now_add
Automatically set the field to now when the object is first created. Useful for creation of
timestamps. Note that the current date is always used; it's not just a default value that
you can override.
'''

def __str__(self):
        return self.text
