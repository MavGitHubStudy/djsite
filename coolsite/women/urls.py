import women.views as w
from django.urls import path  # re_path


urlpatterns = [
    path('', w.WomenHome.as_view(), name='home'),
    path('about/', w.about, name='about'),
    path('addpage/', w.AddPage.as_view(), name='add_page'),
    path('contact/', w.contact, name='contact'),
    path('login/',  w.login, name='login'),
    path('post/<slug:post_slug>/', w.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', w.WomenCategory.as_view(),
         name='category'),
]
