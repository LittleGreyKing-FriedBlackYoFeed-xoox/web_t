from django.contrib import admin
from django.conf.urls import *
from allModel.userdemo.userViews import index,register,userList
from allModel.xiaohuihui.studentViews import student
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< Updated upstream
from allModel.jz.jzViews import jz
from allModel.zhangshuting.zzViews import students
=======

from allModel.zhaojiawei.zzView import rename

>>>>>>> Stashed changes
urlpatterns = [
    url('admin/', admin.site.urls),
    url('^index/$',index),
    url('^register/$',register),
    url('^userList/$',userList),
    url('^student/$',student),
<<<<<<< Updated upstream
    url('^jz/$',jz),
    url('^shuting/$',students),
=======
    url('^xxxx/$',rename),
>>>>>>> Stashed changes
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
