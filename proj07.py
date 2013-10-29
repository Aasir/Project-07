def read(filename):
    while True:
        try:
            x = open(filename + '.txt')
            x.readline()
            MI = {}
            for line in x:
                county = line[153:239]
                county = county.strip()
                county = county[:((county.find('County')-1))]
                county = county.lower()
                count_children = int(line[48:57])
                perc_children = float(line[75:80])
                median = int(line[132:139])
                if county in MI:
                    print('Error Detected')
                else:
                    MI[county] = (count_children,perc_children,median)
            return MI
            break
        except IOError:
            print('Cannot open File')
            print('Closing Program')
            exit()
                            
## Column 8 [48:57]
## Column 11 [75:80]
## Column 20 [132:139]
## Column for county [153:239]

def print_highest_data(Dict):
    highest = 0
    Hkey = None
    for k.v in Dict.items():
        if (v > highest):
            highest = v
            Hkey = k
    print_data(Hkey,Dict)

def print_lowest_data(Dict):
    lowest = 100
    Lkey = None
    for k,v in Dict.items():
        if (v < lowest):
            lowest = v
            Lkey = k
    print_data(Lkey,Dict)

def print_county_data(name, Dict):
    name = name.lower()
    for k,v in Dict.items():
        if (k == name):
            x = k
    print_data(k,Dict)
            

def print_data(name, Dict):
    name = name.lower()
##    if name == None or name == "":
##        do somethign special
    if name in Dict:
        print("{}: {} {} {}".format(name.capitalize() + ' County',Dict[name][0],Dict[name][1],Dict[name][2]))
    else:
        print(name.capitalize()," County is not situated in Michigan")
        
            
    
        
        
        

filename = input('Please Enter Filename: ')
MI = read(filename)

while True:
    if (filename == 'q') or (filename == 'Q'):
        print("Exiting the Program")
        exit()
    else:
        key = input("Please Enter the County Data you want to see: ")
        print_county_data(key,MI)
    
