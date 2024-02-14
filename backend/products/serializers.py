from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, id):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()