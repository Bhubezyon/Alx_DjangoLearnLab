# Permissions and Groups Setup

This app uses Django's built-in permissions and groupsto manage access:

## Custom Permissions
Defined in 'Book' models:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- **Viewers**: can_view
- **Editors**: can_crerate, can_edit
- **Admins**: all permissions

## Enforcement
Views are protected using '@permissions_reqired' decorators.

## Testing 
Assign users to groupsvia Django Admin and verifyaccess to views.