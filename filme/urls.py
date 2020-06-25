from django.urls import path

from .views import list_filme, create_filme, update_filme, delete_filme

urlpatterns = [
    path('', list_filme, name='list_filme'),
    path('new', create_filme, name='create_filme'),
    path('update/<int:id>/', update_filme, name='update_filme'),
    path('delete/<int:id>/', delete_filme, name='delete_filme'),
]
