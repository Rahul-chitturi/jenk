
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('standardResults.xml')

# Get the root element
root = tree.getroot()

average_elements = root.findall('.//average')

# Calculate the average value
total_sum = 0
count = 0
for average_element in average_elements:
    average_value = int(average_element.text)
    total_sum += average_value
    count += 1

average = total_sum / count

print(round(average))
