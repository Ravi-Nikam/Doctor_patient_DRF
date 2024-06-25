# # permissions.py
from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return request.user.is_authenticated and request.user.user_type == 'D'
