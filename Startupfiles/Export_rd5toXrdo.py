import os
import xml.etree.ElementTree as ET

# Function to read the .rd5 file as text and extract relevant information
def read_rd5_file(rd5_filename):
    data = {}
    try:
        with open(rd5_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                # Look for key-value pairs in the file
                if '=' in line:
                    key, value = line.split('=', 1)
                    data[key.strip()] = value.strip()
        return data
    except Exception as e:
        print(f"Error reading .rd5 file: {e}")
        return None

# Function to create an OpenDRIVE .xodr file from extracted data
def create_xodr_from_rd5(data, xodr_filename):
    # Start creating the OpenDRIVE XML structure
    xodr_root = ET.Element("OpenDRIVE")

    road_network = ET.SubElement(xodr_root, "roadNetwork")
    
    # Use data from .rd5 to create a simple road (simplified version)
    road = ET.SubElement(road_network, "road", id="1", name="Converted Road")
    
    # Create a lane section (simplified example)
    lane_section = ET.SubElement(road, "laneSection", s="0.0")
    lane = ET.SubElement(lane_section, "lane", id="1", type="driving")

    # Add geometry (simplified example, you may need more details from the .rd5 data)
    geometry = ET.SubElement(lane_section, "geometry", x="0.0", y="0.0", hdg="0.0", length=data.get("RoadNetworkLength", "1000"))

    # Ensure the directory exists
    os.makedirs(os.path.dirname(xodr_filename), exist_ok=True)

    # Save the OpenDRIVE .xodr file
    xodr_tree = ET.ElementTree(xodr_root)
    xodr_tree.write(xodr_filename, encoding="UTF-8", xml_declaration=True)
    print(f"OpenDRIVE file saved as {xodr_filename}")

# Main function to convert .rd5 to .xodr
def convert_rd5_to_xodr(rd5_filename, xodr_filename):
    # Step 1: Read .rd5 file and extract data
    rd5_data = read_rd5_file(rd5_filename)
    
    if rd5_data:
        # Step 2: Create OpenDRIVE file based on the extracted data
        create_xodr_from_rd5(rd5_data, xodr_filename)
    else:
        print("Failed to read .rd5 file.")

# Example Usage: Save the file in the specified folder
rd5_filename = "/var/lib/jenkins/workspace/cSimulation/Data/Road/lanechange.rd5"
xodr_filename = "/var/lib/jenkins/workspace/cSimulation/Data/Road/traffic1.xodr"

convert_rd5_to_xodr(rd5_filename, xodr_filename)
