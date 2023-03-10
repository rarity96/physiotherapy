from django.urls import path
from . import views
from website import views as ex_views
urlpatterns = [
    path('', ex_views.Home.as_view(), name='home'),
    path('contact/', ex_views.Contact.as_view(), name='contact'),
    path('blog/', ex_views.Blog.as_view(), name='blog'),
    path('blog_single/', ex_views.BlogSingle.as_view(), name='blog-single'),
    path('services/', ex_views.Services.as_view(), name='services'),
    path('about/', ex_views.About.as_view(), name='about'),

]
