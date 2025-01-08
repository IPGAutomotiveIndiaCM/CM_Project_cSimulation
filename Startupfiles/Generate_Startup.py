import subprocess
import sys

# Define the command and parameters to run
command = [
    '/opt/ipg/carmaker/linux64-13.1.1/bin/osc2cm',  # Path to the osc2cm executable
    '--cmprojpath', '/var/lib/jenkins/workspace/cSimulation',  # Path to the CM project
    '--oscfname', '/var/lib/jenkins/workspace/cSimulation/Data/OpenSCENARIO/Overtaker.xosc',  # OpenSCENARIO file
    '--validate',  # Validate flag
    '--egoname', 'Ego',  # Ego name
    '--trfname', 'Overtaker',  # Trajectory file name
    '--rdfname', 'Overtaker_road',  # Road file name
    '--egoinf', 'demoo',  # Ego vehicle info
    '--egoinf', ' DemoCar',
    '--trfendmode', '2',  # Trajectory end mode
    '--loglevel', '4',  # Log level
    '--logtofile',  # Log to file
    '--logtoconsole',  # Log to console
    '--trfmobj',  # Traffic object flag
    "--trajlegacy",
    "--defaultman","999s"
]

try:
    # Run the command
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the output to console
    print("Command executed successfully:")
    print(result.stdout)
except Exception as e:
    # General exception handling
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

filem= "Startup_Example_Template"                     # Original file
lookup = 'nv.Speed = '
lookup_1 = 'nv.Lateral_Offset = '         
lookup_5 = 'kv.SimParameters\:DStore.OutPath = SimOutput/Overtake_'  

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
