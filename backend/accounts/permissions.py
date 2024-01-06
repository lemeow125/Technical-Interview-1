from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagerOrReadOnly(BasePermission):
    message = "You must be a manager to perform this action."

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_manager
        )
