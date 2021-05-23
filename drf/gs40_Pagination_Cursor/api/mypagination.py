from rest_framework.pagination import CursorPagination


# Custom Pagination: Recommended
class MyCursorPagination(CursorPagination):
    page_size = 8
    # default ordeing is by created, if created is not in model, error is thrown. To overcome the error we must order by other field as done below.
    ordering = 'name'
    cursor_query_param = 'cur'

