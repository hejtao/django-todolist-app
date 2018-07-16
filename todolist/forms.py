# -- coding: utf-8 --
from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=50,
                           widget=forms.TextInput( attrs={
                                                           'class' : 'form-control',
                                                           'placeholder' : '请输入新任务的名称',
                                                           'aria-label' : 'Todo',
                                                           'aria-describedby' : 'add-btn'
                                                    '''       'autocomplete' : "off"   关闭提示框   '''       }))

class TodoTextArea(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "91", 'rows': "4", 'placeholder' : '请编辑任务内容' }))
