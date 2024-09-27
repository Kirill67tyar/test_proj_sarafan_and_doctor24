from rest_framework.permissions import IsAuthenticated


class IsAuthenticatedAndOwner(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return bool(obj.cart.owner == request.user)
