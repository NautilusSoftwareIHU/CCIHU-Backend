from rest_framework.permissions import IsAuthenticated, BasePermission

class IsActive(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous
                    and request.user.active)


class IsInactive(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous
                    and not request.user.active)


class IsAnonymous(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_anonymous)