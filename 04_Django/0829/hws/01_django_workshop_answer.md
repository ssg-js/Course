## 1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<str:menu>/<int:people>/', views.dinner),
]
```



## 2. pages/views.py

```python
from django.shortcuts import render

def dinner(request, menu, people):
    context = {
        'menu': menu, 
        'people': people,
    }
    return render(request, 'dinner.html', context)
```



## 3. templates/dinner.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>저녁 메뉴 추천</title>
</head>
<body>
  <h1>저녁 메뉴</h1>
  <h2>저녁 먹을 사람?! {{ people }}명</h2>
  <h2>어떤 메뉴?! {{ menu }}</h2>
</body>
</html>
```
