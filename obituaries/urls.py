from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_obituary, name='submit_obituary'),
    path('view/', views.view_obituaries, name='view_obituaries'),
    path('<int:id>/', views.obituary_detail, name='obituary_detail'),  # Detail view URL
]
