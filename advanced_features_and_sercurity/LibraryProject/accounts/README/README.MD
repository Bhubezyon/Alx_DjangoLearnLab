#  Permission and Groups Setup

## Custom Permissions
Define in 'Book' model:
- 'can_view'
- 'can_create'
- 'can_edit'
- 'can_delete'

## Views
Each view is protected using '@permission_required' decorators.

## Testing 
Assign ussers to group and verify access to views manually.

## Location 
All code is in 'advanced_features_and_sercurity/'

#  Django Sercurity Enhancements

## settings.py
- DEBUG = False
- CSRF_COOKIE_SECURE, SESSIONS_COOKIE_SECURE = True
- X_FRAME_OPTIONS = 'DENY'
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True
- CPS headers via django-csp or manual injection

## Templates
- All forms include '{% csrf_token %}'

## Views
- ORM used for queries
- User input validated via Django forms

## Testing
- Manual form submission with test users
- Inspect cookies for 'Secure' flag
- Use browser dev tools to verify CSP headers
