from django.shortcuts import render,render_to_response,HttpResponse
from allModel.xiaohuihui import studentModel

# 访问首页
def student(request):
    student_list = studentModel.Student.objects.all()
    return render(request, "xiaohuihui/studentIndex.html", {"student_list": student_list})