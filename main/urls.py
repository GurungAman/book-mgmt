from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.log_in, name="login"),

    path("", views.BookListView.as_view(), name="homepage"),
    path("detail/<int:pk>", views.detail, name="detail"),

    path('book_api/', views.BookView.as_view()),
    path('book_api/<int:pk>/', views.BookView.as_view()),

    path('logout/', views.logout_view, name='logout'),

]
