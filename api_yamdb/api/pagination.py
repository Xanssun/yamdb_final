# flake8: noqa
from rest_framework import pagination
from rest_framework.response import Response


class LimitOffsetCustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response({

            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
