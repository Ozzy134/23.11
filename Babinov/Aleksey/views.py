from django.shortcuts import render
from django.http import HttpResponse

def index(request, fio, age, hobby):
    return HttpResponse(f'ФИО: {fio}, возраст: {age}, хобби: {hobby}')

def about(request, sity, uspex, yesorno):
    return HttpResponse(f'Приехал из города: {sity}, успеваемость в школе: {uspex}, Учиться: {yesorno}')

def contacts(request, nick, tg, number):
    return HttpResponse(f'Никнейм на github: {nick}, tg: {tg}, Номер телефона: {number}')