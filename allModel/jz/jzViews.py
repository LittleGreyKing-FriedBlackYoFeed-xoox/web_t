from django.shortcuts import render,render_to_response
from  allModel import userModel

def jz(requests):
    return render_to_response("jz/jz.html")