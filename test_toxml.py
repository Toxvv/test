import os
import xml.dom.minidom

from xml.dom.minidom import parse
xml_file = r'new.xml'
# #拿到根节点
domTree = parse(xml_file)
rootNode = domTree.documentElement

print(domTree.toxml())  # 使用制表符作为缩进
print('***********')
print(rootNode.toxml())