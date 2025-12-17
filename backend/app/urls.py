from django.urls import path
from . import views

urlpatterns = [
    path('portfolios/', views.NoteListCreate.as_view(), name='note-list'),
    path('portfolios/delete/<int:pk>/', views.NoteDelete.as_view(), name='delete-note'),
]


