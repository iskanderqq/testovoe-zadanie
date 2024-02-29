from django.shortcuts import render
from .models import Product,Lesson,Group
from django.db.models import Count
import datetime

# Create your views here.
def get_product_list():
    products = Product.objects.annotate(num_lessons=Count('lesson'))
    data = []
    for product in products:
        data.append({
            'creator': product.creator,
            'name': product.name,
            'date_of_start': product.date_of_start,
            'time_of_start': product.time_of_start,
            'price': product.price,
            'num_lessons': product.num_lessons
        })
    return data

def get_lessons(request, product_id):
    lessons = Lesson.objects.filter(product_id=product_id)
    data = []
    for lesson in lessons:
        data.append({
            'name': lesson.name,
            'url': lesson.url
        })
    return data

def user_to_group(request, product_id):
    if request.method == 'POST':
        groups = Group.objects.filter(product_id=product_id)
        product = Product.objects.get(id=product_id)

        if product.date_of_start > datetime.timezone.now().date():
            for group in groups:
                current_users_count = group.students.count()
                if current_users_count < group.product.max_users:
                    group.students.id = request.user.id
                    #Дальнейшее добавление пользователя
