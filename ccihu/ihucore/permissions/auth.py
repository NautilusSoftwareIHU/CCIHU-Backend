from rest_framework.permissions import IsAuthenticated, BasePermission

class IsActive(IsAuthenticated):
    def has_Permission(self, request, view):
        return bool(request.user and not request.user.is_anonymous
                    and request.user.active)
    


class IsInactive():
    def has_Permission(self, request, view):
        if(IsActive.has_Permission()):
            return False
        else:
            return True

class IsAnonymous():
    def has_permission(self, request, view):
        return bool(request.user.is_anonymous)