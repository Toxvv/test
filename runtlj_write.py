import os
import xml.etree.ElementTree as ET
import datetime
import sys
from xml.dom.minidom import Document 
gnss_orbit_data = {
    'G01': {
        datetime.datetime(2024, 3, 27, 12, 0, 0): {'L': 1.0, 'B': 2.0, 'H': 3.0},
        datetime.datetime(2024, 3, 27, 13, 0, 0): {'L': 2.0, 'B': 3.0, 'H': 4.0}
    },
    'G02': {
        datetime.datetime(2024, 3, 27, 12, 0, 0): {'L': 3.0, 'B': 4.0, 'H': 5.0},
        datetime.datetime(2024, 3, 27, 13, 0, 0): {'L': 4.0, 'B': 5.0, 'H': 6.0}
    }
}
plot_doc = Document()
plot_tlj_doc = plot_doc.createElement('plot')
gnss_orbit_doc = plot_doc.createElement('gnss_orbit')
for gnss_prn in gnss_orbit_data:
    print(gnss_prn)
    gnss_prn_doc = plot_doc.createElement('sat')
    gnss_prn_doc.setAttribute('prn',gnss_prn)
    for dt in gnss_orbit_data[gnss_prn]:
        print(dt)
        time_str = dt.strftime('%Y-%m-%d %H:%M:%S')

        gnss_orbit_prn_doc = plot_doc.createElement('orbit')
        gnss_orbit_prn_doc.setAttribute('time',time_str)

        pos_line = str(gnss_orbit_data[gnss_prn][dt]['L']) + ',' + str(gnss_orbit_data[gnss_prn][dt]['B']) + ',' +\
            str(gnss_orbit_data[gnss_prn][dt]['H'])

        # gnss_pos_doc = plot_doc.createElement('position')
        gnss_orbit_prn_doc.appendChild(plot_doc.createTextNode(pos_line))
        # gnss_orbit_prn_doc.appendChild(gnss_pos_doc)

        gnss_prn_doc.appendChild(gnss_orbit_prn_doc)
    gnss_orbit_doc.appendChild(gnss_prn_doc)

plot_tlj_doc.appendChild(gnss_orbit_doc)
plot_doc.appendChild(plot_tlj_doc)
f = open('test.xml', "w+") 
f.write(plot_doc.toprettyxml(indent=" ")) 
f.close()