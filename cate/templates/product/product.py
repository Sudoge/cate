'''
提取产品素材
'''
from lxml import etree
import json
import random

prod_list = [
    ('玫瑰香酥西兰花', 'Rose fried broccoli'),
]

with open('index.html', 'r') as f:
    content = f.read()
html = etree.HTML(content)
# 产品节点
node_list = html.xpath('//main[4]/ul[2]/li')
product_list = list()
for node in node_list:
    product_dict = {}
    product_dict['zh_name'] = prod_list[0][0]
    product_dict['en_name'] = prod_list[0][1]
    product_dict['price'] = random.randint(10,100)
    product_dict['img_src'] = node.xpath('./a/img/@src')[0]
    # 保存到文件
    with open('product.json','a') as f:
        print('ok')
        str_prod = json.dumps(product_dict, ensure_ascii=False)
        f.write(str_prod + ',\n')