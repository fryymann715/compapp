
import os


def get_comp_txt():
    print("Opening comppdf...")
    compfile = open('pdfminer/comppdf.txt')
    print("Reading comptxt...")
    comptxt = compfile.read()
    compfile.close()
    return comptxt


def extract_comps(comptxt):
    comp_start = comptxt.find("********   COMPS   ********")
    comptxt = comptxt[comp_start:]
    return comptxt


def get_specific_comp(comptxt, comp_type):
    comp_start = comptxt.find("*********  " + comp_type + "   *********")
    comp_end = comptxt.find("Total " + comp_type + ":")
    comp_50 = comptxt[comp_start:comp_end]
    print comp_50







test = get_comp_txt()

test2 = extract_comps(test)

get_specific_comp(test2, "Service")
