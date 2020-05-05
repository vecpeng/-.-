import json

import xlrd
import xlwt

from xlutils.copy import copy

xlrd.Book.encoding ="utf-8"
# 读取一个Excel文件 可以是一个空的excel文件 最好用xls  xlsx格式容易报错
readbook = xlrd.open_workbook(u'data.xls')

writebook = copy(readbook)

new_sheet = writebook.get_sheet(0)

# 读取json
with open("chenpeng.json",encoding='utf-8') as json_file:
    data = json.load(json_file)

# 遍历json里的新闻
for index, news in enumerate(data):
    print(news)
    # 给指定行、指定列写入指定内容
    new_sheet.write(index, 0, index)
    new_sheet.write(index, 1, news['id'])
    new_sheet.write(index, 2, news['news_title_translate_en'])
    new_sheet.write(index, 3, news['news_position'])
   

# 保存写入的内容
writebook.save('data.xls')
