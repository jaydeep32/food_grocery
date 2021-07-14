from django.core.management.base import BaseCommand 
from django.utils.text import slugify
from bs4 import BeautifulSoup
from product.models import Product
import requests
import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        res = requests.get(r"https://www.lovefood.com/gallerylist/81561/the-worlds-most-delicious-dishes-youll-want-to-try")
        soup = BeautifulSoup(res.text, 'html.parser')
        articles  = iter(soup.find_all("div", {'class': 'gallery__slider'}))   
        next(iter(articles))
        for i in articles:
            price = random.randint(50, 200)
            title = i.find('h2', {'class': 'gallery__caption-title'}).text
            src = i.find('img')['src']
            description = i.find('div', {'class': 'gallery__caption'}).text
            Product.objects.get_or_create(title=title, image=src, description=description, price=price, slug=slugify(title))

