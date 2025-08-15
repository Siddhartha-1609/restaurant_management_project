from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Item
from .serializers import ItemSerializer

#for now hardcoded one with simple django temp without API
try:
    from products.models import Menu
except ImportError:
    Menu = None

def menu(request):
    if Menu:
        menu_items_qs = Menu.objects.all()
        if menu_items_qs.exists():
            menu_items = [item.name for item in menu_items_qs]
        else:
            menu_items = ["Marga Pizza" , "Peperoni Pizza" , "Ceaser salad" , "Pasta Carbarona"]
    else:
        menu_items = ["Marga Pizza", "Peperoni Pizza", "Ceaser salad" , "Pasta Carbarona"]
    
    context ={
        "menu_items" : ["Marga Pizza", menu_items,
        "restaurant_name" : settings.RESTAURANT_NAME,
    }
    return render(request,"menu_list.html",context)

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
