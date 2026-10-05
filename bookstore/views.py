from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import Book, Category
from .forms import BookForm


def is_staff(user):
    """Only logged-in staff/admin may add, edit or delete books."""
    return user.is_authenticated and user.is_staff


def book_list(request):
    """Show all books, with optional category filter and search."""
    books = Book.objects.all()
    categories = Category.objects.all()

    # Category filter from ?category=slug
    category_id = request.GET.get("category")
    if category_id:
        books = books.filter(category_id=category_id)

    # Search from ?q=...
    query = request.GET.get("q")
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    return render(
        request,
        "bookstore/book_list.html",
        {
            "books": books,
            "categories": categories,
            "current_category": int(category_id) if category_id else None,
            "query": query or "",
        },
    )


def book_detail(request, pk):
    """Show a single book's full details."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, "bookstore/book_detail.html", {"book": book})


@user_passes_test(is_staff, login_url='login')
def book_create(request):
    """Add a new book (staff only)."""
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" added successfully!')
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm()
    return render(request, "bookstore/book_form.html", {"form": form, "title": "Add Book"})


@user_passes_test(is_staff, login_url='login')
def book_update(request, pk):
    """Edit an existing book (staff only)."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, "Book updated successfully!")
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "bookstore/book_form.html", {"form": form, "title": "Edit Book"})


@user_passes_test(is_staff, login_url='login')
def book_delete(request, pk):
    """Delete a book (staff only, with confirmation)."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect("book_list")
    return render(request, "bookstore/book_confirm_delete.html", {"book": book})
