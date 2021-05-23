from rest_framework.pagination import LimitOffsetPagination


# Custom Pagination: Recommended
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5 # if limit not provided by client, this is default limit
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit =7
    # offset is the number, after which records should be listed
    

