
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('aggregate-results.xml')

# Get the root element
root = tree.getroot()

empty_group = root.find(".//Group[@label='']")

if empty_group is not None:
    # Fetch the avg_rt tag value
    avg_rt_value = empty_group.find("avg_rt").attrib['value']

    print(round(float(avg_rt_value) * 1000))
