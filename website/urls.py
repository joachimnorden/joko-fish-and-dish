from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationList.as_view(), name='home'),
    path('index', views.index, name='index'),
    path('manage', views.manage, name='manage'),
    path('book-a-table', views.book_a_table, name='book-a-table'),
]
