### 简介
![](https://upload-images.jianshu.io/upload_images/1863961-a042f1e9226309e8.JPG?imageMogr2/auto-orient/strip%7CimageView2/2/w/540)

![](https://upload-images.jianshu.io/upload_images/1863961-f2620a3760390d86.JPG?imageMogr2/auto-orient/strip%7CimageView2/2/w/540)

![](https://upload-images.jianshu.io/upload_images/1863961-c8481445ffdc31d4.JPG?imageMogr2/auto-orient/strip%7CimageView2/2/w/540)

### 软件版本

- Django 1.8.19
- Python 2.7
- psycopg2 2.7.5 ( Postgresql 9.6.9 )
- Bootstrap 4.1.2

### 功能清单
 - 创建新任务
    - 创建后立即进入任务设置页面
    - 设置截止时间，优先级，任务具体内容（默认截止时间为生成时间，默认优先级为3）
    - 保存后自动进入该任务所在分页
    - 任务名为空警告
    
![](https://upload-images.jianshu.io/upload_images/1863961-3bebd0fe03ed24c7.gif?imageMogr2/auto-orient/strip)

- 标记任务为已完成
    - 标记后自动进入该任务所在的分页
    - 撤销标记

![](https://upload-images.jianshu.io/upload_images/1863961-b8c7fae4b9a2e47f.gif?imageMogr2/auto-orient/strip)

- 支持优先级排序和截止时间排序（若两者都开启，后开启的生效；若两者都关闭，则按生成的先后顺序排列）

![](https://upload-images.jianshu.io/upload_images/1863961-7cb5d0841a5f7104.gif?imageMogr2/auto-orient/strip)

![](https://upload-images.jianshu.io/upload_images/1863961-bee11bffa71b61bb.gif?imageMogr2/auto-orient/strip)

- 返回上级页面

![](https://upload-images.jianshu.io/upload_images/1863961-342cb3455d2fe383.gif?imageMogr2/auto-orient/strip)


- 删除当前任务、删除所有已完成任务、清空所有任务

![](https://upload-images.jianshu.io/upload_images/1863961-050974f51dc679e6.gif?imageMogr2/auto-orient/strip)

![](https://upload-images.jianshu.io/upload_images/1863961-d7380669ce3abd4f.gif?imageMogr2/auto-orient/strip)
