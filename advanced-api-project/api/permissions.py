from rest_framework.permissions import BasePermission,

permission_classes = [IsAdminOrReadOnly]

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'HEAD'] or request.user.is_staff # SAFE_METHOD are GET, HEAD, OPTIONS
        
    