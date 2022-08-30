from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    context = {
        'name': 'alex',
        'foods': ['apple', 'burger'],
    }
    return render(request, 'greeting.html', context)


def base(request):
    return render(request, 'base.html')


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    department = request.GET.get("department")
    name = request.GET.get('name')

    if department == '대전 2반':
        if name == '김영주':
            message = '교수님이시군요!'
        else:
            message = '교육생이시군요!'
    else:
        message = '다른 반이시군요!'

    return render(request, 'catch.html', context)
