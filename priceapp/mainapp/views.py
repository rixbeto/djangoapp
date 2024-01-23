from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from .models import (Product, Notification)
import simplejson
import random 

class Home(TemplateView):

    def get(self, request):
        return JsonResponse({})
    
class ProductList(TemplateView):

    def get(self, request):
        product = Product.objects.all()
        items = [
            {
                'id':p.id,
                'name':p.product_name,
                'price':f"${p.price}",
                }
                  for p in product
            ]
        return JsonResponse(items, safe=False)

class GetProduct(TemplateView):

    def get(self, request, name=None):
        product = Product.objects.filter(product_name__icontains=name)
        items = [
            {
                'id':p.id,
                'name':p.product_name,
                'price':f"${p.price}",
                }
                  for p in product
            ]
        return JsonResponse(
            {'items': product.count(), 'data': items},
            safe=False)

class SetProductUser(TemplateView):
    
    def post(self, request):
        response = {}
        items = simplejson.loads(request.body)
        for i in items.get('products'):
            notification = Notification(
                user_id=items.get('user'),
                product_id=i, watch=False)
            notification.save()
        return JsonResponse(response, safe=False)


class GetNotification(TemplateView):

    def get(self, request):
        notifications = Notification.objects.filter(user_id=request.user.id)
        notifications = [
            {'product__name':n.product.product_name}
            for n in notifications
            ]
        return JsonResponse(notifications, safe=False)



class ChangePrice(TemplateView):

    def get(self, request):
        prods = Product.objects.all()
        for p in prods:
            new_price = random.randrange(10,1340)
            status = "rise"
            if new_price < p.price:
                status = "dropped"
                p.notification_set.all().update(watch=False)
            p.price = new_price
            p.status = status
            p.save()
        return JsonResponse({}, safe=False)


class WatchNotification(TemplateView):

    def get(self, request, n=None):
        notification = Notification.objects.get(id=n)
        notification.watch = True
        notification.save()
        return JsonResponse({})

class CreateProducts(TemplateView):

    def get(self, request):
        brands = ['Iphone' ,'Galaxy Tab', 'Xiaomi', 'ZTE', 'Lenovo']
        versions = ['1', '1.5', '14', '20', '8' , '12' , '45', '8', '9b', '12 pro', '20 x']
        for x in range(10):
            bone_product = {
                'product_name':f'{random.choice(brands)} {random.choice(versions)}',
                'price': random.randrange(100,1340),
                'status': 'set',
                }
            product = Product(**bone_product)
            product.save()
        return JsonResponse({})