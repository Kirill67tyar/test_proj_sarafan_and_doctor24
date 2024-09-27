from functools import wraps

from rest_framework import status
from rest_framework.response import Response


def check_auth_for_swagger(view):
    @wraps(view)
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED
            )
        return view(request, *args, **kwargs)
    return inner
