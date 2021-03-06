
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )



class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 4


class PostPageNumberPagination(PageNumberPagination):
    page_size = 20
