
from django.shortcuts import get_object_or_404
from .forms import CommentForm,CreateUserForm
from django.http.response import JsonResponse
from itertools import chain
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render,redirect
from .serializers import PostSerializer
from django.core.paginator import Paginator 
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth import authenticate,login
from django.views.generic.base import TemplateView
from .models import(
    Welcom,
    category,
    Post,
    Comment,
    shop,
    ShopCategory,
    Doctors,
    video,
    categoryfirst,
    CategoryLast,
    pagetext
    
)




class Index_View(TemplateView):
    
    template_name = "mainapp/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["v"] = Welcom.objects.last()
        return context
    

class News_View(TemplateView):
    
    template_name = "mainapp/news.html"
    
def Category_View(request,slug):
    
    cat = category.objects.get(slug=slug)
    
    catfirst = categoryfirst.objects.all()
    
    return render(request,"mainapp/category.html",{"cat":cat,"catfirst":catfirst})

class News_page_View(ListView):
    paginate_by = 3
    model = Post

    template_name = "mainapp/news_page.html"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    
def serch(request):
    
    if searched := request.GET.get("s", None):
        articleobjects = Post.objects.filter(
            Q(title__icontains=searched) | Q(text__icontains=searched)
        ).distinct()
    

    return render(request,"mainapp/news_page.html",{"news_search":articleobjects,"searched":searched })
    
def News_page_get_View(request,id):
    
    post = get_object_or_404(Post, id=id)   
    if request.method == "POST":
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()

            return redirect("News_page_get_View", id=post.id)
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = CommentForm()


  
    
    context = {
        "post": post,
        "form": form,
    }
    
    return render(request, "mainapp/post.html",context)
  
    
class Post_View(TemplateView):
    template_name = "mainapp/post.html"
    
    

class Aboutas_View(TemplateView):
    
    template_name = "mainapp/aboutas.html"    
   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["v"] = Welcom.objects.last()
        return context

class PostPagination(PageNumberPagination):
    page_size = 1

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    
def shop_View(request):

    # contact_list = shop.objects.all()



    category = request.GET.get("category")

    if category == None:
        shopi = shop.objects.all() 
    else:
        shopi = shop.objects.filter(category__title=category)
    
    a = request.GET.get("ordring-minus")   
    if a:
        shopi = shop.objects.all().order_by("-id")
    categoryi = ShopCategory.objects.all()
    
    a = request.GET.get("ordring")
    if a == "cheap-expensive":
        shopi = shop.objects.all().order_by("price")
    if a == "expensive-cheap":
        shopi = shop.objects.all().order_by("-price")

       
    paginator = Paginator(shopi,3 )  
   
    page_number = request.GET.get("page")
    shopi = paginator.get_page(page_number)     


    

    
    if searched := request.GET.get("s", None):
    
        shopi = shop.objects.filter(
            title__icontains=searched
        ).distinct()
    
    context = {
        "searched": searched,
        "category_shop":categoryi,
        "shop":shopi,
        # "mian":k
    }
            
        
    return render(request,"mainapp/shop.html",context)
    
      

def contact_View(request):
    form = CreateUserForm()
     
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,"Account was created for" + user )
            
            
    
    return render(request,"mainapp/contact.html",{"form":form })

def login_View(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("Index_View")
        else:
            messages.info(request,"ape vopshem logini teqstna")
    return render(request,"mainapp/login.html")

# class search_View(TemplateView):
    
#     template_name = 'mainapp/search.html'

class  Media_View(TemplateView):
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["video"] = video.objects.all()
        return context
    
    
    template_name = 'mainapp/media.html'

class search_View(ListView):
    template_name = 'mainapp/search.html'
    paginate_by = 20
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        
        if query is not None:
            blog_results        = Post.objects.search(query)
            lesson_results      = Doctors.objects.search(query)
            shop_results        = shop.objects.search(query)
            
            queryset_chain = chain(
                    blog_results,
                    lesson_results,
                    shop_results
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs)
            return qs

        return Post.objects.none()    
def categorylast(request,slug):
    
    catlast = categoryfirst.objects.get(slug=slug)
    
    products = CategoryLast.objects.filter(keylast=catlast)
    if products:
        return render(request,"mainapp/categoryfirst.html",{"products":products })
    else:
        return render(request,"mainapp/categorylast.html",{"catlast":catlast})


    

