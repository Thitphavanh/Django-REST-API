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




#POST Data (save data to database)
@api_view(['POST'])
def post_product(request):
	if request.method == 'POST':
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

			
		

data = [
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'M',
		'quantity': '100',
		'price': '250000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'L',
		'quantity': '150',
		'price': '250000'
	},
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'XL',
		'quantity': '100',
		'price': '250000'
	},
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Liverpool FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Liverpool.jpg',
		'size': 'XXL',
		'quantity': '80',
		'price': '250000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'M',
		'quantity': '100',
		'price': '290000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'L',
		'quantity': '100',
		'price': '290000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'XL',
		'quantity': '100',
		'price': '290000'
	},

	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'XL',
		'quantity': '100',
		'price': '290000'
	},
	{
		'detail': 'New jersey 2022/2023',
		'name': 'Manchester United FC',
		'imagePath': 'https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/man-united.jpg',
		'size': 'XXL',
		'quantity': '100',
		'price': '290000'
	}
]


def Home(request):
	return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
