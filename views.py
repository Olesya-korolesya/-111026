# #Задание 1
# from django.shortcuts import render
#
# def index(request):
#     fruits = ['Яблоки', 'Груши', 'Сливы', '']
#     return render(request, 'blog/profile.html', context={'fruits':fruits})

# #Задание 2
# from django.shortcuts import render
#
# def multiplication_table(request):
#     return render(request, 'blog/profile.html', {
#         'nums': range(1, 10)
#     })

# #Задание 3
#
# from django.shortcuts import render
#
# def items_list_view(request):
#     items = [
#         {'name': 'Карточка 1'},
#         {'name': 'Карточка 2'},
#         {'name': 'Карточка 3'},
#         {'name': 'Карточка 4'},
#         {'name': 'Карточка 5'},
#     ]
#     chunked_items = [items[i:i + 3] for i in range(0, len(items), 3)]
#
#     return render(request, 'blog/profile.html', {'rows': chunked_items})

# #Задание 4
#
# from django.shortcuts import render
#
# def cities_list_view(request):
#
#     cities = sorted(["Москва", "Саратов", "Воронеж", "Краснодар"])
#
#     return render(request, 'blog/profile.html', {'cities': cities})
#

# #Задание 5
#
# from django.shortcuts import render
#
#
# def students_list_view(request):
#
#     students = ['Иванов Иван', 'Петров Петр', 'Сидоров Сидор', 'Федор Федоров']
#
#     return render(request, 'blog/profile.html', {'students': students})


# #Задание 6
#
# from django.shortcuts import render
#
# def tags_list_view(request):
#
#     tags = ['python', 'django', 'html']
#
#     context = {
#         'tags': tags
#     }
#
#     return render(request, 'blog/profile.html', context)

# #Задание 7
#
# from django.shortcuts import render
#
# def countdown_view(request):
#     steps = ['Старт', 'Разгон', 'Взлёт']
#     return render(request, 'blog/profile.html', {'steps': steps})


# #Задание 8
#
# from django.shortcuts import render
#
# def news_list(request):
#   news = [ 'Новости экономики', 'Новости погоды', 'Городские новости' ]
#   return render(request, 'blog/profile.html', {'news': news})

# # Задание 9
# from django.shortcuts import render
#
# def student_grades_view(request):
#
#     grades = {
#         'Иванов': [5, 4, 5],
#         'Петров': [3, 4, 2],
#     }
#     return render(request, 'blog/profile.html', {'grades': grades})

# # Задание 10
#
# from itertools import groupby
# from operator import itemgetter
# from django.shortcuts import render
#
# def products_list_view(request):
#     products = [
#         {'name': 'Персики', 'category': 'Фрукты'},
#         {'name': 'Груши', 'category': 'Фрукты'},
#         {'name': 'Кабачки', 'category': 'Овощи'},
#     ]
#
#     grouped = {}
#     for key, group in groupby(products, key=itemgetter('category')):
#         grouped[key] = list(group)
#
#     return render(request, 'blog/profile.html', {'grouped_products': grouped})