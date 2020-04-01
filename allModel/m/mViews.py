from django.shortcuts import render,render_to_response,HttpResponse

# 访问首页
def me(request):
    return render_to_response("m/m.html")