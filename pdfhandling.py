
import os


comp_type = {0: "Cold Food", 1: "Service", 2: "Time", 3: "Quality", 4: "Didn't Like",
             5: "Alcohol", 6: "TM Error"}

comp_txt_file = open(r'pdfminer/comps.txt')

# Pull the text from the pdf file.
def get_comp_txt():
    print("Opening File...")
    compfile = open('pdfminer/paymentdetail.txt')
    print("Reading File...")
    comptxt = compfile.read()
    line = compfile.readline()
    print line
    compfile.close()
    print("Closing File...")
    return comptxt


# Pull the comps section from the payment details file
def extract_comps(comptxt):
    print("Locating comps within file...")
    comp_start = comptxt.find("********   COMPS   ********")
    comptxt = comptxt[comp_start:]
    print("Comps located...")
    return comptxt


# Pulls the specific comp type from the comp file.

def get_specific_comp(compfile, comp_type):
    print("Fetching " + comp_type + " comps...")
    print("     Reading File.")
    lynes = compfile.readlines()
    comp_locator = "*********  " + comp_type + "   *********\n"
    comp_ender = "Total " + comp_type + ":\n"
    new_list = lynes[lynes.index(comp_locator):lynes.index(comp_ender)+1]
    print("     Comps found and extraced.")
    #new_list = new_list.remove("\n")
    print new_list
    return new_list


# Iterates through the given text and pulls the needed items

def pull_comps(comp_list):
    comp_dict = {}
    check_number = []
    new_comps = []

    for lyne in comp_list:
        lyne = lyne.rstrip()
        if lyne.isdigit():
            lyne = int(lyne)
            if lyne >= 1000:
                check_number.append(lyne)
    max_counter = len(check_number)
    print check_number
    counter = 0
    while counter < 3:
        new_comp = []
        checknum = comp_list.index(str(check_number[counter])+'\n')
        new_comp.append(comp_list[checknum])
        manager = checknum+4
        new_comp.append(comp_list[manager])
        price = manager + 6
        new_comp.append(comp_list[price])
        server = price + 4
        new_comp.append(comp_list[server])
        itemname = server + 4
        new_comp.append(comp_list[itemname])
        counter += 1
        new_comps.append(new_comp)
    print new_comps
    print len(new_comps)

    #print new_comp


def get_all_comps(comptxt):
        counter = 0
        current_comps = {}
        while counter < 7:
            current_comps[comp_type[counter]] = get_specific_comp(comptxt, comp_type[counter])
            counter += 1
        return current_comps


# time_comps = pull_comps()

cf_comp = get_specific_comp(comp_txt_file, comp_type[2])
print pull_comps(cf_comp)


# print comp_dict[comp_type[2]]
print " "
print " "
# print time_comps


