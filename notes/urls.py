from django.urls import path
from .views import index, delete_note

urlpatterns = [
    path('', index, name='index'),        
    path('delete/<int:id>', delete_note, name='delete'),        
        
        
]

