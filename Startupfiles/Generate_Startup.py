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

