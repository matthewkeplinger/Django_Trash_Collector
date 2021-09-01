from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.daily_view, name="index"),
    path('create/', views.create, name="create"),
    path('daily_view/', views.daily_view, name='daily_view'),
    path('day_filter/', views.choose_day, name='day_filter'),
    path('confirm/<int:user_id>', views.confirm, name = 'confirm')
]