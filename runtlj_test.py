import xml.etree.ElementTree as ET
import datetime
xml_file='obs_sim.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

for child in root:
    print(child.text)
    if child.tag == 'start_time':
        datetime_str = child.text
        start_time = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    elif child.tag == 'arc_length':
        ses_length = int(float(child.text))
    elif child.tag == 'fit':
        fit = int(float(child.text))
    elif child.tag == 'gnss_dir':
        gnss_dir = child.text
    elif child.tag == 'sim_sp3_file':
        sim_sp3_file = child.text
    elif child.tag == 'gnss_system':
        gnss_system_str = child.text
        gnss_system = gnss_system_str.split(',')
    elif child.tag == 'sid_threshold':
        sid_threshold = float(child.text)
    elif child.tag == 'phase_noise':
        phase_noise = float(child.text)/10.0
    elif child.tag == 'pseudo_noise':
        pseudo_noise = float(child.text)/10.0
    elif child.tag == 'cut_off':
        cut_off = float(child.text)
    elif child.tag == 'output':
        work_dir = child.text
    elif child.tag == 'error_file':
        error_file = child.text
    elif child.tag == 'bin_dir':
        bin_dir = child.text