from rest_framework.pagination import PageNumberPagination


# Custom Pagination: Recommended
class MyPageNumberPagination(PageNumberPagination):
    
    page_size = 5 # items per page
    
    page_query_param = 'pg' # replaces 'page' with 'pg' as search parameter(one used in browser in address)
    # http://127.0.0.1:8000/studentapi/?pg=2
    
    page_size_query_param = 'records' # decides the size of page, client can use it
    # http://127.0.0.1:8000/studentapi/?pg=2&records=7

    max_page_size = 7 # page size cannot be set more than 7 now, a value of records(defined above) set more than value here doesn't go beyond this value

    # last_page_strings = 'last' # replaces pg=last with pg=end, for getting last page

