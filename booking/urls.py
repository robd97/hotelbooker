from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('locations/', views.locations, name='locations'),
    path('reservation/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservation/new/', views.reservation_new, name='reservation_new'),
    path('reservation/new/<str:city>/', views.reservation_new, name='reservation_new'),
    path('reservation/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'),
    path('reservation/<int:pk>/cancel/', views.reservation_cancel, name='reservation_cancel'),
    path('hotels/', views.hotels, name='hotels'),
    path('employees/', views.employee_details, name='employee_details'),
]