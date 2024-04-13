import xml.dom.minidom
from xml.dom.minidom import parse
# 在内存中创建一个空的文档
doc = xml.dom.minidom.Document()

# 创建根元素
root = doc.createElement('booklist')
# print('添加的xml标签为：',root.tagName)

# 设置根元素的属性
root.setAttribute('type', 'science and engineering')

# 将根节点添加到文档对象中
doc.appendChild(root)

# 创建子元素
book = doc.createElement('book')
# 添加注释
book.appendChild(doc.createComment('这是注释'))

# 设置子元素的属性
book.setAttribute('category', 'math')

# 子元素中嵌套子元素，并添加文本节点
title = doc.createElement('title')
title.appendChild(doc.createTextNode('learning math'))
author = doc.createElement('author')
author.appendChild(doc.createTextNode('张三'))
pageNumber = doc.createElement('pageNumber')
pageNumber.appendChild(doc.createTextNode('561'))

# 将子元素添加到boot节点中
book.appendChild(title)
book.appendChild(author)
book.appendChild(pageNumber)
# 将book节点添加到root根元素中
root.appendChild(book)

# 创建子元素
book = doc.createElement('book')
# 设置子元素的属性
book.setAttribute('category', 'python')

title = doc.createElement('title')
title.appendChild(doc.createTextNode('learning python'))

author = doc.createElement('author')
author.appendChild(doc.createTextNode('李四'))
pageNumber = doc.createElement('pageNumber')
pageNumber.appendChild(doc.createTextNode('600'))

# 将子元素添加到boot节点中
book.appendChild(title)
book.appendChild(author)
book.appendChild(pageNumber)
# 将book节点添加到root根元素中
root.appendChild(book)

#print(root.toxml())
print(doc.toprettyxml())
fp = open(r'new.xml', 'w', encoding='utf-8')  # 需要指定utf-8的文件编码格式，不然notepad中显示十六进制
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
fp.close()

