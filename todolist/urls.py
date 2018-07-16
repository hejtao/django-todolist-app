# -- coding: utf-8 --
from django.conf.urls import url
from . import views

 # 第三个 edit 与 redirect('')一直，第二个为函数名，第一个与html的 href="{% url "edit" %}" 一致

urlpatterns = [
    url(r'^$', views.index, name='index'),       # 访问 localhost 将调用 views 的 index 方法，index在 .html中代表该url
    url(r'^add/$', views.addTodo, name='add'),        # 访问 localhost\add 将调用 views 的 addTodo 方法
    url(r'^complete/page(?P<todo_id>[0-9]+)/$', views.completeTodo, name='complete'),
    url(r'^discomplete/page(?P<todo_id>[0-9]+)/$', views.disComplete, name='discomplete'),
    url(r'^deletecompleted/$', views.deleteCompleted, name='deletecompleted'),
    url(r'^deleteall/$', views.deleteAll, name='deleteall'),
    url(r'^edittask/page(?P<todo_id>[0-9]+)/$', views.editTask, name='edittask'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^deletethis/$', views.deletethis, name='deletethis'),
    url(r'^submitbody/$', views.submitbody, name='submitbody'),
    url(r'^start_edition/$', views.start_edition, name='start_edition'),
    url(r'^order_by_pri_btn/$', views.orderByPriBtn, name='order_by_pri_btn'),
    url(r'^order_by_date_btn/$', views.orderByDateBtn, name='order_by_date_btn'),
]
