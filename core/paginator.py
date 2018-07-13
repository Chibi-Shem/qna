from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict

class MyPaginator(pagination.PageNumberPagination):
	
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('total_pages', self.page.paginator.num_pages)
        ]))
