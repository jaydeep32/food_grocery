from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    # path('login/<str:go_next>/', views.login, name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]




