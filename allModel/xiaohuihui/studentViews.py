from django.shortcuts import render,render_to_response


# 访问首页
def student(request):
    return render_to_response("xiaohuihui/studentIndex.html")
