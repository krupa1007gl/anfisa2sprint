# ice_cream/admin.py
from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper

empty_value_display = 'Не задано'

class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
    IceCreamInline,
    )
    list_display = (
        'title',
    )

class IceCreamAdmin(admin.ModelAdmin):
    filter_horizontal = ('toppings',)

    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)

admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)