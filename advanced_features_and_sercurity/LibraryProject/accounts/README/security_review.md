# Security Review: HTTPS and Secure Header

## HTTPS Enforcement
- All HTTP traffic is redirected to HTTPS using 'SECURE_SSL_REDIRECT'.
- HSTS is enabled for one year with preload and subdomain support.

# Cookie Sercurity
- 'SESSION_COOKIE_SECURE' and 'CSRF_COOKIE_SECURE' ensure cookies are only sent over HTTPS.

## Secure Headers 
- 'X_FRAME_OPTIONS = DENY' prevents clickjacking.
- 'SECURE_CONTENT_TYPE_NOSNIFF' blocks MIME-type sniffing.
- 'SECURE_BROWSER_XSS_FILTER' activate browser-side XSS protection.

# Deployment
- SSL/TLS configured via Nginx with strong ciphers and redirect rule.
- Certificates managed via Let's Encrypt or custom CA.

## Next Steps
- Monitor SSL cert expiry.
- Consider adding CSP headers for further XSS mitigation
- Use tools like [Mozilla Observatory] (https://observatory.mozilla.org/) or [SecurityHeaders.com] (https://sercurityheaders.com/) to audit headers.