from django.db import models

# Author model model stores basic author information
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Book model stores title, publication year, and links to an Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"    

# Author model repressenta writerwith a name.
# Book model includes a title, publication year, and a foreign key to Author.
# The relationship is one-to-many: one author can have multiple books.