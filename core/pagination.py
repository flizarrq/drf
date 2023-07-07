import Response as Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math


class PagePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'size'
    max_page_size = 15

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count / self.get)
        return Response({
            'total_items': count,
            'total_pages':
        })

