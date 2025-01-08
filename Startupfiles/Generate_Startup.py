import subprocess
import os

# Define the paths
osc2cm_path = "/opt/ipg/carmaker/linux64-13.1.1/bin/osc2cm"
cmprojpath = "/var/lib/jenkins/workspace/cSimulation"
oscfname = "/var/lib/jenkins/workspace/cSimulation/Data/OpenSCENARIO/Overtaker.xosc"
log_dir = "/var/lib/jenkins/workspace/cSimulation/SimOutput/OSC2CM_Log/"
template_vehicle_dir = "/opt/ipg/carmaker/linux64-13.1.1/Data/Traffic/Template/1_Vehicles/Geely_Emgrand_Boyue_2016"
overtaker_a1_dir = "/var/lib/jenkins/workspace/cSimulation/Data/Traffic/Template/Overtaker_A1"

# Check if the directories exist, if not, create them
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

# Ensure directories are accessible by creating them if they don't exist
create_directory_if_not_exists(log_dir)
create_directory_if_not_exists(template_vehicle_dir)
create_directory_if_not_exists(overtaker_a1_dir)

# Set the permissions for the directories
def set_permissions(directory):
    try:
        subprocess.run(['sudo', 'chmod', '-R', '755', directory], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting permissions for {directory}: {e}")

# Set permissions for necessary directories
set_permissions(log_dir)
set_permissions(template_vehicle_dir)
set_permissions(overtaker_a1_dir)

# Construct the osc2cm command
command = [
    'sudo', osc2cm_path,  # Add sudo here to run the command with elevated privileges
    '--cmprojpath', cmprojpath,
    '--oscfname', oscfname,
    '--validate',
    '--egoname', 'Ego',
    '--trfname', 'Overtaker',
    '--rdfname', 'Overtaker_road',
    '--egoinf', 'demoorr',
    '--trfendmode', '2',
    '--loglevel', '4',
    '--logtofile',
    '--logtoconsole',
    '--trfmobj',
    '--trajlegacy',
    '--defaultman', '999s'
]

# Function to run the command
def run_command(command):
    try:
        print("Running command:", " ".join(command))
        subprocess.run(command, check=True)
        print("Command executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

# Run the osc2cm command
run_command(command)



filem= "Startup_Example_Template"                     # Original file
lookup = 'nv.Speed = '
lookup_1 = 'nv.Lateral_Offset = '         
lookup_5 = 'kv.SimParameters\:DStore.OutPath = SimOutput/LaneChangeISO_'  

file1 = open(filem)
all_lines = file1.readlines()
l_num = open(filem).read()[:open(filem).read().index(lookup)].count('\n')
l_num1 = open(filem).read()[:open(filem).read().index(lookup_1)].count('\n')
l_num5 = open(filem).read()[:open(filem).read().index(lookup_5)].count('\n')

arr = all_lines[l_num].split()
arr1 = all_lines[l_num1].split()
arr_5 = all_lines[l_num5].split()

def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))


a_list = list(range(60, 80, 10))   # range of values to be changed each time
b_list = list(range(2, 4, 1))
for x in a_list:  # for every value in the range
    for y in b_list:
        with open(filem, 'r', encoding='utf-8') as file:
            data = file.readlines()
        data[l_num] = lookup + str(x) + '\n'
        data[l_num1] = lookup_1 + str(y) + '\n'
        data[l_num5] = lookup_5 + 'speed_' + str(x) + 'LatOff_' + str(y) + '\n'
        
        with open(filem + 'S_'+str(x) +'_O_'+ str(y), 'w', encoding='utf-8') as file:
            file.writelines(data)

