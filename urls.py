from main.views import (
    Index_View,
    News_View,
    Category_View,
    News_page_View,
    Post_View,
    News_page_get_View,
    Aboutas_View,
    PostViewSet,
    shop_View,
    contact_View,
    login_View,
    search_View,
    Media_View,
    categorylast
    
)
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    # path("",index,name="index")
    path("",Index_View.as_view(),name="Index_View"),
    path("news/",News_View.as_view(),name="News_View"),
    path("shop/",shop_View,name="shop_View"),
    path("News_page_View/",News_page_View.as_view(),name="News_page_View"),
    path("aboutas/",Aboutas_View.as_view(),name="Aboutas_View"),
    path("contact/",contact_View,name="contact_View"),
    path("search/",search_View.as_view(),name="search_View" ),
    path("Media/",Media_View.as_view(),name="Media_View"),
    path("login_View/",login_View,name="login_View"),
    path("Post_View/<int:id>/",Post_View.as_view(),name="Post_View"),
    path("News_page_get_View/<int:id>/",News_page_get_View,name="News_page_get_View"),
    path("",include(router.urls)),
    path("categorylast/<slug:slug>/",categorylast,name="categorylast"),
    path("<slug:slug>/",Category_View,name="Category_View"),
]
