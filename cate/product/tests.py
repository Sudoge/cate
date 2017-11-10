# from django.test import TestCase
# from product.models import ProductModel
# import random
# # Create your tests here.
#
# prod_list = [
#     {"en_name": "Rose fried broccoli", "zh_name": "玫瑰香酥西兰花", "img_src": "images/foodlist1.jpg", "price": 25},
#     {"en_name": "Rose fried broccoli", "zh_name": "玫瑰香酥西兰花", "img_src": "images/foodlist2.jpg", "price": 10},
#     {"en_name": "Rose fried broccoli", "zh_name": "玫瑰香酥西兰花", "img_src": "images/foodlist3.jpg", "price": 13},
#     {"en_name": "Rose fried broccoli", "zh_name": "玫瑰香酥西兰花", "img_src": "images/foodlist4.jpg", "price": 19},
#     {"en_name": "Rose fried broccoli", "zh_name": "玫瑰香酥西兰花", "img_src": "images/foodlist5.jpg", "price": 60},
#     {"en_name": "Rose fried broccoli", "zh_name": "玫瑰香酥西兰花", "img_src": "images/foodlist6.jpg", "price": 78},
# ]
#
# for i in range(100):
#     prod = ProductModel()
#     index = random.randint(0, len(prod_list)-1)
#     prod.en_name = prod_list[index]['en_name']
#     prod.zh_name = prod_list[index]['zh_name']
#     prod.image = prod_list[index]['img_src']
#     prod.price = prod_list[index]['price']
#     prod.save()


from product.models import BannerModel
import random

names = [
    '西红柿拌鸡蛋',
    '百味卤鸡腿',
    '清蒸红薯'
]

images = [
    'images/banner.jpg',
    'images/banner2.jpg',
    'images/banner3.jpg'
]


for i in range(10):
    banner = BannerModel()
    banner.ad_name = random.choice(names)
    banner.ad_image = random.choice(images)
    banner.save()