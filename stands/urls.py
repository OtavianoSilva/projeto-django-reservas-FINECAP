from django.urls import path
from .views import StandTemplateView, StandListView, StandDetailView, StandFormView, StandDeleteView, StandUpdateView


urlpatterns = [
    path('home', StandTemplateView.as_view(), name='stands_home'),
    path('stands/', StandListView.as_view(), name='stands'),
    path('cria_stand', StandFormView.as_view(), name='cria_stand'),
    path('stands_detail/<pk>', StandDetailView.as_view(), name='stands_detail'),
    path('stands_detail/<pk>/delete_stand', StandDeleteView.as_view(), name='delete_stand'),
    path('stands_detail/<pk>/update_stand', StandUpdateView.as_view(), name='update_stand'),
]