from django.shortcuts import render,render_to_response


# 访问首页
def students(request):
    return render_to_response("zhangshuting/zzTest.html")
