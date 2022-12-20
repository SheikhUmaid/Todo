
from django.urls import path
from .views import TodoList, TodoDetail
urlpatterns = [
    path('', TodoList.as_view()),   # /api/
    path('<int:pk>/', TodoDetail.as_view()),  # /api/1
    
    ]
