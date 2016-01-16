
import os


comp_type = {0: "Cold Food", 1: "Service", 2: "Time", 3: "Quality", 4: "Didn't Like",
             5: "Alcohol", 6: "TM Error"}


# Pull the text from the pdf file.
def get_comp_txt():
    print("Opening File...")
    compfile = open('pdfminer/paymentdetail.txt')
    print("Reading File...")
    comptxt = compfile.read()
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


# Pulls the specific comp type from the comp text.
def get_specific_comp(comptxt, comp_type):
    print("Fetching " + comp_type + " comps...")
    comp_start = comptxt.find("*********  " + comp_type + "   *********")
    comp_end = comptxt.find("Total " + comp_type + ":")
    comps = comptxt[comp_start:comp_end]
    print("Finished.")
    return comps


# Iterates through the given text and pulls the needed items
def pull_comps(comptxt):
    comp_dict = {}
    for line in comptxt:



    return comp_dict


def get_all_comps(comptxt):
        counter = 0
        current_comps = {}
        while counter < 7:
            current_comps[comp_type[counter]] = get_specific_comp(comptxt, comp_type[counter])
            counter += 1
        return current_comps

payment_detail_text = get_comp_txt()
comp_all_text = extract_comps(payment_detail_text)
comp_dict = get_all_comps(comp_all_text)

time_comps = pull_comps(comp_dict[comp_type[2]])


print comp_dict[comp_type[2]]
print " "
print " "
print time_comps


