import shutil
from .LBLdistrifillHR import distrifill_rename, gebruik_shutill_en_verplaats_file_van
from Path_actions.path_actions import *
import pandas as pd

glob_dwd_pdf = sorted(PDF_bestanden_map.rglob("*.pdf"))
vila_xml = sorted(vila_xmls.rglob("*.xml"))

# vila_basis_xml =[path for path in vila_xml if len(path.stem) == 9]
vila_basis_xml =[path for path in vila_xml]

xml = vila_basis_xml[7]

esko_product_itemnumber = pd.read_xml(xml, dtype=str ,xpath="./EskoProducts/EskoProduct")["ProductNo"][0]

esko_product_name = pd.read_xml(xml, xpath="./EskoProducts/EskoProduct")["ProductName"][0]

esko_product_reference = pd.read_xml(xml, dtype=str,xpath="./EskoProducts/EskoProduct")["CustomerProductReference"][0]

# xml_df = pd.read_xml(xml, xpath="./Customer")
xml_job_df = pd.read_xml(xml, xpath="./Job")

xml_EP_df = pd.read_xml(xml, xpath="./EskoProducts/EskoProduct")


# klant_ref = xml_df['CustomerJobReference'][0]
vila_ORDER_num = xml_job_df['OrderId'][0]
# geeft alle itemnummers in df
vila_ITEM_nummers = xml_EP_df["ProductNo"][0]
shapes = xml_EP_df["Shape"]


# dwd = [path for path in vila_basis_xml]

def vila_ordernummer(padxml):
    customer = pd.read_xml(padxml, dtype=str, xpath="./Job")["CustomerJobReference"][0]
    return customer


def customernum(padxml):
    customer = pd.read_xml(padxml, dtype=str, xpath="./Customer")["CustomerJobReference"][0]
    return customer


def Mnumber(padxml):
    customer_M = pd.read_xml(padxml, dtype=str, xpath="./EskoProducts/EskoProduct")["CustomerProductReference"][0]

    return customer_M


def item_number(padxml):
    customer_M = pd.read_xml(padxml, dtype=str, xpath="./EskoProducts/EskoProduct")["ProductNo"][0]
    return customer_M




def tuple_destinies(gekozen_pad,dictionairy,key):
    """ looking with key in dictionairy to find the original path
    pad_naar esko should be  the original path on G: esko products etc (is a dynamicic nbaming fuction)"""

    pad_naar_esko_dyn = pad_naar_item_nummer_folder_maker(dictionairy[key][1])


    bestandsnaam = str(dictionairy[key][0] + ".pdf")
    originalpad = PDF_bestanden_map.joinpath(bestandsnaam)
    # dest1 = pad_naar_esko.joinpath((str(customernum_dict[key][1]) + ".pdf"))
    dest1 = pad_naar_esko_dyn
    dest2 = gekozen_pad.joinpath((str(dictionairy[key][1]) + ".pdf"))
    twee_adres_paren = [(originalpad, dest1), (originalpad, dest2)]
    return twee_adres_paren

# builds a list With Paths from the dictionairy customer_dict
# two_tuple_pair_list = [tuple_destinies(key) for key in customernum_dict]

#moves the files to a collecting folder for easy insertion in labelhub
# and one that places them in esko.
# moving = [(gebruik_shutill_en_verplaats_file_van(tuplelist[0]),
#            gebruik_shutill_en_verplaats_file_van(tuplelist[1]))
#           for tuplelist in two_tuple_pair_list]

# moving = [gebruik_shutill_en_verplaats_file_van(tuplelist[0])
#           for tuplelist in two_tuple_pair_list]

