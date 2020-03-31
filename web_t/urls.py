from django.contrib import admin
from django.conf.urls import *
from allModel.userdemo.userViews import index,register,userList
from allModel.xiaohuihui.studentViews import student
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('admin/', admin.site.urls),
    url('^index/$',index),
    url('^register/$',register),
    url('^userList/$',userList),
    url('^student/$',student),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
