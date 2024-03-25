import xml.etree.ElementTree as ET

# 解析XML文件
tree = ET.parse('example.xml')
root = tree.getroot()

# 遍历每个country元素
for country in root.findall('country'):
    # 获取country元素的name属性值
    country_name = country.get('name')
    print('Country:', country_name)

    # 获取country元素下的子元素的文本内容
    rank = country.find('rank').text
    year = country.find('year').text
    gdppc = country.find('gdppc').text
    print('Rank:', rank)
    print('Year:', year)
    print('GDP per Capita:', gdppc)

    # 遍历neighbor元素
    print('Neighbors:')
    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        neighbor_direction = neighbor.get('direction')
        print(neighbor_name, neighbor_direction)

    print()
