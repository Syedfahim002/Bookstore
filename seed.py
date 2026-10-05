"""Seed some demo books/categories so the site has content to show.
Run with:  python manage.py shell < seed.py
"""
from bookstore.models import Category, Book

cats = ["Fiction", "Science", "Programming", "History", "Biography"]
created = [Category.objects.get_or_create(name=n)[0] for n in cats]

demo_books = [
    ("The Python Programming Language", "Guido van Rossum", "Programming", 350),
    ("Django for Beginners", "William Vincent", "Programming", 450),
    ("Flutter Complete Guide", "Maximilian", "Programming", 550),
    ("A Brief History of Time", "Stephen Hawking", "Science", 420),
    ("The Alchemist", "Paulo Coelho", "Fiction", 299),
    ("Sapiens", "Yuval Noah Harari", "History", 480),
    ("Clean Code", "Robert C. Martin", "Programming", 520),
    ("Steve Jobs", "Walter Isaacson", "Biography", 399),
]

cat_map = {c.name: c for c in created}
for title, author, cat, price in demo_books:
    Book.objects.get_or_create(
        title=title,
        defaults={
            "author": author,
            "category": cat_map[cat],
            "price": price,
            "description": f"A great book titled '{title}' — added as demo data.",
        },
    )

print(f"Seeded {len(Category.objects.all())} categories and {len(Book.objects.all())} books.")