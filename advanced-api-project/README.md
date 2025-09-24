# API Endpoints

- 'GET /api/books' - List all books (public)
- 'GET /api/books/{id}/' - Retrieve book by ID (public)
- 'POST /api/books/create/' - Create book (auth required)
- 'PUT /api/books/{id}/update/' - Update book (auth required)
- 'DELETE /api/books/{id}/delete/' - Delete book (auth required)

## Permissions

- Authenticated usres can create, update, and delete.
- Unauthenticated users can read only
