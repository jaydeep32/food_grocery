from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save   
from django.dispatch import receiver
from django.utils.text import slugify

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse("product:product-detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return f"{self.title} - {self.id}"

@receiver(pre_save, sender=Product)
def slug_save(sender, instance, *args, **kwargss):
    instance.slug = slugify(instance.title)
    
# pre_save.connect(slug_save, sender=Product)



