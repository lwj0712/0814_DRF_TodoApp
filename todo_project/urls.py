from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),  # 'todo' 앱의 URL 포함
    path('', include('todo.urls')),  # 웹 페이지 관련 URL 패턴
]
