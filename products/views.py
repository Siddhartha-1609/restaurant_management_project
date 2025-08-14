from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''
def menu(request):
    context ={
        "menu_items" = ["Marga Pizza", "Peperoni Pizza","Ceaser salad","Pasta Carbarona"],
        "restaurant_name" = settings.RESTAURANT_NAME,
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
