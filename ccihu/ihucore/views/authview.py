from rest_framework.views import APIView
from ihucore.permissions.auth import IsAuthenticated
from ihucore.permissions.auth import IsActive, IsInactive, IsAnonymous

class AuthView(APIView):
    permission_classes = (IsAuthenticated,)

class AnonymousOnlyView(APIView):
    permission_classes = (IsAnonymous,)

class InactiveOnlyView(APIView):
    permission_classes = (IsInactive, )

class IHUBaseView(APIView):
    permission_classes = (IsActive,IsAuthenticated,)