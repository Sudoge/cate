
from django.template import Library

register = Library()

@register.filter()
def get_num_list(index, total_pages):
    '''分页显示,每个页面只显示10个可点击页面'''
    list = []
    print(total_pages)
    page_nums = 10
    if index <= 5 :
        for i in range(1,page_nums+1):
            list.append(i)
        return list

    if index > 5 and index+int(page_nums/2)+1 <= total_pages:
        for i in range(index-int(page_nums/2)+1, index+int(page_nums/2)+1):
            list.append(i)
    else:
        for i in range(total_pages-page_nums, total_pages+1):
            list.append(i)

    return list

