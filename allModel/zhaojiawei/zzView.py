from django.shortcuts import render_to_response


def rename(request):
    return render_to_response("user/index.html")


def ZhuanYe(request):
    return render_to_response("Elephant/manageweb.html")