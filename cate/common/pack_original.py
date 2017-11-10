
def get_param(request, key):
    return request.GET.get(key, 1)