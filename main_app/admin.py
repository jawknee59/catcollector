from django.contrib import admin

# import your models here
from .models import Cat, Feeding, Toy, Photo

# Register your models here.
admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Photo)
admin.site.register(Toy)