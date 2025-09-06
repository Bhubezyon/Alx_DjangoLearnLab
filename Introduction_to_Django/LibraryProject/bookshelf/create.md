###     creating a Book Instance

'''python
Book.objects.create(
    title="Clean Code",
    author="Robert C. Martin",
    published_date="2008-08-01",
    isbn="9780132350884",
    pages=464,
    language="English"
)