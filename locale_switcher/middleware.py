
class LocaleSwitcherMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.resolver_info = (view_func, view_args, view_kwargs)
        return None
