from django.urls import path
from . import views
from website import views as ex_views
urlpatterns = [
    path('', views.home, name='home'),
    path('/contact', ex_views.Contact.as_view(), name='contact'),
    path('/blog', ex_views.Blog.as_view(), name='blog'),
    path('/blog_single', ex_views.BlogSingle.as_view(), name='blog-single'),

]
