from django.urls import path
from .import views


urlpatterns=[
    path("content",views.show_blog,name='viewblogs'),
    path("contentdetails/<int:myid>",views.show_blog_details,name='viewblogs'),
    path("userContentDetails/<int:myid>",views.show_user_blog_details,name='viewblogs'),
    path('createblog',views.createblog,name="crating a blog"),
    path('comment',views.comment,name='blog comments'),
    path('publishcomment',views.publish_comment,name='blog comments'),
    path('search',views.search,name='searching blog'),
    path('signup',views.signup,name="user signup"),
    path('login',views.userLogin,name="user login"),
    path('logout',views.userLogout,name="user logout")
]