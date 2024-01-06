from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagerOrReadOnly(BasePermission):
    message = "You must be a manager to perform this action."

    def has_permission(self, request, view):
        # Allow safe methods regardless of whether the user is authenticated or not
        if request.method in SAFE_METHODS:
            return True

        # Check if the user is authenticated
        elif not request.user or not request.user.is_authenticated:
            return False

        # Check if the user is a manager
        return request.user.is_manager
