from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


# GET Data
@api_view(['GET'])
def all_product(request):
	allproduct = Product.objects.all()
	serializer = ProductSerializer(allproduct, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)




data = [
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'M',
		'stock': '100',
		'price': '250000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'L',
		'stock': '150',
		'price': '250000'
	},
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'XL',
		'stock': '100',
		'price': '250000'
	},
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'XXL',
		'stock': '80',
		'price': '250000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'M',
		'stock': '100',
		'price': '290000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'L',
		'stock': '100',
		'price': '290000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'XL',
		'stock': '100',
		'price': '290000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'XL',
		'stock': '100',
		'price': '290000'
	},
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'pathImages': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'XXL',
		'stock': '100',
		'price': '290000'
	}
]


def Home(request):
	return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
