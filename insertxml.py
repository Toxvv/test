import os
import xml.dom.minidom

from xml.dom.minidom import parse

# 对book.xml新增一个子元素english，并删除math元素
xml_file = r'new.xml'

# #拿到根节点
domTree = parse(xml_file)
rootNode = domTree.documentElement

rootNode.removeChild(rootNode.getElementsByTagName('book')[0])

print(rootNode.toxml())

# 在内存中创建一个空的文档
doc = xml.dom.minidom.Document()

book = doc.createElement('book')
book.setAttribute('category', 'english')
title = doc.createElement('title')
title.appendChild(doc.createTextNode('learning english'))
author = doc.createElement('author')
author.appendChild(doc.createTextNode('王五'))
pageNumber = doc.createElement('pageNumber')
pageNumber.appendChild(doc.createTextNode('328'))

book.appendChild(title)
book.appendChild(author)
book.appendChild(pageNumber)

math_book = rootNode.getElementsByTagName('book')[0]

# insertBefore方法  父节点.insertBefore(新节点，父节点中的子节点)
rootNode.insertBefore(book, math_book)
# appendChild将新产生的子元素在最后插入
# rootNode.appendChild(book)

#print(rootNode.toxml())

with open(xml_file, 'w', encoding='utf-8') as fh:
    domTree.writexml(fh, indent='', addindent='\t', newl='', encoding='utf-8')