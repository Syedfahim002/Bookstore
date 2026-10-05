from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all()
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "category",
            "category_id",
            "price",
            "description",
            "cover",
            "created_at",
        ]