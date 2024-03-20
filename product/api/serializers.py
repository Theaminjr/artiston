from rest_framework import serializers
from product.models import Product,ProductDetail,ProductImage,TableRow


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        exclude = ['product']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ['product']

class TableRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableRow
        exclude = ['product']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer()
    table_rows = TableRowSerializer()
    details = ProductDetail()

    class Meta:
        model = Product
        exclude = []

