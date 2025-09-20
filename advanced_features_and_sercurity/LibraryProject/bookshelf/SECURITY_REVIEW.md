# HTTPS and Security Configuration Review

## Django Settings

- 'SECURE_SSL_REDIRECT': Enforces HTTPS
- 'SECURE_HSTS_SECONDS': Enables HSTS for 1 year
- 'SESSION_COOKIE_SECURE' & 'CSRF_COOKIE_SECURE': Secure cookies
- 'X_FRAME_OPTIONS', SECURE_CONTENT_TYPE_NOSNIFF', SECURE_BROWSER_XSS_FILTER: Securew headers

## Deployment
- SSL/TLS configured via Nginx/Apache
- Certificates issued via Let's Encrypt

## Manual Tests
- HTTP requests redirect to HTTPS
- Cookies marked as Secure
- Headers visible in browser dev tools 