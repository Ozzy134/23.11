from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, kwargs = {'fio': 'Бабинов Алексей Евгеньевич', 'age': '16', 'hobby': 'фото'}),
    path('about', views.about, name='about', kwargs = {'sity': 'Город-герой Волгоград', 'uspex': 'Нормальная', 'yesorno': 'Люблю'}),
    path('contacts', views.contacts, name='contacts', kwargs = {'nick': 'Ozzy134', 'tg': '@lexababnv', 'number': '89047568690'}),
]