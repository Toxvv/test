from xml.dom.minidom import Document

# 创建 XML 文件
def create_xml(filename):
    doc = Document()

    # 创建根元素
    root = doc.createElement("travel_guide")
    doc.appendChild(root)

    # 国家、城市和景点信息
    countries = [
        {"name": "USA", "cities": [
            {"name": "New York", "attractions": ["Statue of Liberty", "Central Park"]},
            {"name": "Los Angeles", "attractions": ["Hollywood", "Disneyland"]}
        ]},
        {"name": "France", "cities": [
            {"name": "Paris", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            {"name": "Nice", "attractions": ["Promenade des Anglais", "Cours Saleya"]}
        ]}
    ]

    # 循环创建国家、城市和景点元素
    for country_info in countries:
        country = doc.createElement("country")
        country_name = doc.createElement("name")
        country_name.appendChild(doc.createTextNode(country_info["name"]))
        country.appendChild(country_name)


        for city_info in country_info["cities"]:
            city = doc.createElement("city")
            city_name = doc.createElement("name")
            city_name.appendChild(doc.createTextNode(city_info["name"]))
            city.appendChild(city_name)


            for attraction_info in city_info["attractions"]:
                attraction = doc.createElement("attraction")
                attraction_name = doc.createElement("name")
                attraction_name.appendChild(doc.createTextNode(attraction_info))
                attraction.appendChild(attraction_name)
                city.appendChild(attraction)
            country.appendChild(city)
        root.appendChild(country)

    # 将 Document 对象保存为 XML 文件
    xml_str = doc.toprettyxml(indent="  ")
    with open(filename, "w") as f:
        f.write(xml_str)


create_xml("travel_guide1.xml")


