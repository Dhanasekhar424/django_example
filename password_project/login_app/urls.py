from django.urls import path
from login_app import views

app_name="login_app"


urlpatterns=[
    #path('admin/',admin.site.urls),
    path('index',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('register',views.register,name='register'),
    path('base/',views.base,name='base'),
    path('link/',views.link,name='link'),
]
