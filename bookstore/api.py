from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    """Full CRUD API for books (GET/POST/PUT/DELETE)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(["GET"])
def category_list(request):
    """List all categories (useful for a Flutter dropdown later)."""
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)