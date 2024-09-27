from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ReadOnlyListModelViewSet(mixins.ListModelMixin,
                               GenericViewSet,):
    http_method_names = [
        'get',
        'options',
    ]
