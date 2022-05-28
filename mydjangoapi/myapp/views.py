from django.shortcuts import render
from django.http import JsonResponse

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
