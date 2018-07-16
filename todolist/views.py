# -- coding: utf-8 --
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.utils.formats import localize       # 日期显示本地语言  django 1.8 还没有

from .models import Todo
from .forms import TodoForm, TodoTextArea

id_buffer = 0
has_warning = False
pri_order_flag = 0
date_order_flag = 0
order_flag = [0, 0]

def index(request):     # 主页 index.html
    global id_buffer
    global has_warning
    global pri_order_flag
    global date_order_flag
    global order_flag

    todo_list = Todo.objects.order_by('id')[::-1]

    if pri_order_flag and date_order_flag:
        if  order_flag == [0,1]:                               # 已开启截止时间排序的情况下，开启优先级排序，按照后开启的排序
            todo_list = Todo.objects.order_by('pri')[::-1]
        else:                                                  # 已开启优先级排序的情况下，开启截止时间排序
            todo_list = Todo.objects.order_by('expire_date')
    else:
        if pri_order_flag:
            todo_list = Todo.objects.order_by('pri')[::-1]

        if date_order_flag:
            todo_list = Todo.objects.order_by('expire_date')

    order_flag = [pri_order_flag, date_order_flag]


    if todo_list:       # 如果任务为空，清空按钮实效
        dis_order_btn = False
        dis_deleteall_button = False
        if Todo.objects.filter(complete__exact=True):
            dis_deletecomplete_button = False
        else:
            dis_deletecomplete_button = True
    else:
        dis_deleteall_button = True
        dis_deletecomplete_button = True
        dis_order_btn = True

    form = TodoForm()

    # 分页器代码从 django 1.8 官方文档拷贝
    paginator = Paginator(todo_list, 5) # Show 5 contacts per page

    page = request.GET.get('page')

    if not page:
        try:           # 当某个任务被删除后，但它的 id 还在 id_buffer 中，将出现 Todo matching query does not exist.
            for i in range(1, paginator.num_pages+1):
                if Todo.objects.get(pk=id_buffer) in paginator.page(i).object_list:
                    page = i
        except:
            page = 1

    contacts = paginator.page(page)

    last_second_page = contacts.paginator.num_pages-1


    context = {
                             'todo_id' : id_buffer,
                         'has_warning' : has_warning,
                                'form' : form,
           'dis_deletecomplete_button' : dis_deletecomplete_button,
                'dis_deleteall_button' : dis_deleteall_button,
                            'contacts' : contacts,
                     'date_order_flag' : date_order_flag,
                      'pri_order_flag' : pri_order_flag,
                       'dis_order_btn' : dis_order_btn,
                    'last_second_page' : last_second_page      }
    has_warning = False


    return render(request, 'todolist/index.html', context)

def edit(request):
    area = TodoTextArea()
    global id_buffer

    todo = Todo.objects.get(pk=id_buffer)
    dis_button = todo.complete      # 根据任务是否完成，给html传递参数，若dis_button = False，完成按钮有效，重启按钮无效，否则反过来

    context = {    'area' : area,
                'todo_id' : id_buffer,
                   'todo' : todo,
             'dis_button' : dis_button,
          'start_edition' : False}
    return render(request, 'todolist/edit.html', context)

def start_edition(request):
    area = TodoTextArea()
    global id_buffer
    todo = Todo.objects.get(pk=id_buffer)
    dis_button = todo.complete      # 根据任务是否完成，给html传递参数，若dis_button = False，完成按钮有效，重启按钮无效，否则反过来

    context = {    'area' : area,
                'todo_id' : id_buffer,
                   'todo' : todo,
             'dis_button' : dis_button,
            'start_edition' : True}
    return render(request, 'todolist/edit.html', context)

@require_POST       # 只接受 POST 方法
def addTodo(request):       # 添加任务
    form = TodoForm(request.POST)
    global id_buffer
    global has_warning

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])  # 添加的新任务，Todo model objec
        new_todo.save()   # 保存 Todo object 到数据库中
        id_buffer = new_todo.pk     # 该函数进入任务编辑页面，用全局变量记录当前任务

        return redirect('start_edition')
    else:
        has_warning = True
        return redirect('index')


@require_POST
def submitbody(request):       # 保存任务数据到数据库
    area = TodoTextArea(request.POST)
    global id_buffer

    todo = Todo.objects.get(pk=id_buffer)
    todo.pri = request.POST['pri']
    if request.POST['expire_date']:
        todo.expire_date = request.POST['expire_date']

    if area.is_valid():
        todo.body = request.POST['body']

    todo.save()

    global has_back_index
    has_back_index = True

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    global has_back_index
    has_back_index = True

    return redirect('index')

def disComplete(request, todo_id):
    global id_buffer
    todo = Todo.objects.get(pk=todo_id)

    new_todo = Todo(text=todo.text)
    new_todo.body = todo.body
    new_todo.compete = False
    new_todo.pri = todo.pri
    new_todo.expire_date = todo.expire_date
    new_todo.save()

    id_buffer = new_todo.pk

    Todo.objects.filter(pk=todo_id).delete()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()      # filter 返回集合

    return redirect('index')

def deleteAll(request):     # 删除所有
    Todo.objects.all().delete()

    return redirect('index')

def editTask(request, todo_id):     # 点击进入任务详情页面时，触发该函数。保存该任务的 id 到全局变量
    global id_buffer
    id_buffer = todo_id

    return redirect('edit')


def deletethis(request):        # 删除当前任务
    global id_buffer
    Todo.objects.filter(pk=id_buffer).delete()

    return redirect('index')


def orderByPriBtn(request):
    global pri_order_flag
    pri_order_flag = int(not pri_order_flag)

    return redirect('index')

def orderByDateBtn(request):
    global date_order_flag
    date_order_flag = int(not date_order_flag)

    return redirect('index')
