from django.shortcuts import render
from django.views import View

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


class Contact(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)


class Blog(View):
    template_name = 'blog.html'

    def get(self, request):
        return render(request, self.template_name)


class BlogSingle(View):
    template_name = 'blog-single.html'

    def get(self, request):
        return render(request, self.template_name)


class Services(View):
    template_name = 'services.html'

    def get(self, request):
        return render(request, self.template_name)


class About(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)
