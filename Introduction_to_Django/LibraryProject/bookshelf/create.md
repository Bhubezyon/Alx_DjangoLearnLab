import os

path = "LibraryProject/bookshelf/create.md
if os.path.isfile(path):
    with open(path, "r")
        content = f.read()
            if "Book.object.create" in content:
                print(File exists and contains the command")
            else:
                print("File exists but command missing")
            
else:
    print(File does not exist")

'''python
Book.objects.create(
    title="Clean Code",
    author="George Orwell",
    published_date="2008-08-01",
    isbn="9780132350884",
    pages=464,
    language="English"
)

