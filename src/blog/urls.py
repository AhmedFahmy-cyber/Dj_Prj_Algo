from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView , CatListView

urlpatterns = [
    path('', views.home, name='home'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('allposts/', views.allposts, name='allposts'),
    path('about/', views.about, name='about'),
    path('formm/', views.formm, name='formm'),
    path('adminapp/<int:app_id>/', views.applist, name='adminapp'),
    path('adminapp/', views.admin_list, name='adminapp'),
    # path('application/', views.adduser, name='application'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('category/<category>', CatListView.as_view(), name='category'),

    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
