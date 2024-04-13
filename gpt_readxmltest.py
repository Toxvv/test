import xml.etree.ElementTree as ET


# 读取 XML 文件并提示内容
def read_xml_and_prompt(filename):
    # 解析 XML 文件
    tree = ET.parse(filename)
    root = tree.getroot()

    # 遍历根元素下的所有子元素
    for child in root:
        # 提示每个子元素的标签和文本内容
        print(f"Tag: {child.tag}, Text: {child.text}")


# 读取 XML 文件并提示内容
read_xml_and_prompt("obs_sim.xml")
