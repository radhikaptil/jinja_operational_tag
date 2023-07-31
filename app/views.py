from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'Ruvee','age':1}
    return render(request,'loop.html',context=d)

def connect(request):
    d={'a':12,'hobbies':['reading','writting']}
    return render(request,'connect.html',context=d)
