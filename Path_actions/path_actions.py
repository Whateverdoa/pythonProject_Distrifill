import re
from datetime import date, timedelta
from pathlib import Path
import datetime
from .pad_namen import *

regexstring_vilaorder = r'\d{9}.xml'
regexstring_vilaitem = r'\d{9}_\d.xml'

# klantnamen lijst en klant-ID lijst ophalen en hieraanhangen voor toekomstig gebruik?
klantnamen = ["HELLOPRINT.B.V", "DRUKWERKDEAL.NL", "PRINT.COM", "VILA ETIKETTEN", "Distrifill"]
klantid =["806321", "569621", "935321", "380321", "982521"]
klantnaam_id_dict = dict(zip(klantnamen,klantid))

itemnum_collection = list(pad_naar_collectie.rglob('*.pdf'))


#todo make this def customer paths
def customer_base_path():
    """with lists of customername and id_number create a dict
    {clientname: client_basepath}"""

    klant_naam_paden = [(WDIR.home().joinpath(ESKO_PRODUCTS, name[0], name)) for name in klantnamen]


def check_jobfolder_with_regex(jobfolder_to_check, jaar):
    # jaar optie is optioneel
    jaar = jaar
    jaar_check = r"(2022)(\d{2})"
    basischeck_verzamelmap = r"\d{6}"  # geeft 6 digits
    jobfolder_is_zes_getallen = len(jobfolder_to_check)
    try:
        jaar_test = re.search(jaar_check, jobfolder_to_check)
        if jaar_test.group(1) == str(jaar) and jobfolder_is_zes_getallen == 6:

            basismap_check_regex = re.search(basischeck_verzamelmap, jobfolder_to_check)
            output_regex_search = basismap_check_regex.group()

            print(f'{output_regex_search = }')
            # return output_regex_search
            return True
        else:
            print(f"vergelijk {jaar_test.group(1)}  met {jaar}")
            print(f'aantal posities (6) van folder = {jobfolder_is_zes_getallen}')
            return False

    except AttributeError:
        print("AttributeError: no Match")
        return False


def find_(hoofd_folder, tijdsduur_in_dagen):
    # todo hoe neem ik het weekeinde mee zonder die 48 uur te gewbruiken
    past_time = date.today() - timedelta(days=tijdsduur_in_dagen)

    folders = []
    for path in Path(hoofd_folder).iterdir():
        timestamp = date.fromtimestamp(path.stat().st_mtime)
        print(f'{timestamp > past_time = }')

        if path.is_dir() and timestamp > past_time and check_jobfolder_with_regex(path.name, 2022):
            print(f'folder: {path}')
            folders.append(path.name)
            print(f"{path.name =}")
            print(path.is_dir())
            # print(WDIR_Job.joinpath(path.name))
            # nieuwdwir = WDIR_Job.joinpath(hoofd_folder)
            # order_nummerpad = nieuwdwir.joinpath(path.name)

    return sorted(folders)


def check_with_regex(the_vila_ordernum_xml, regexstring):
    """there are two kinds of xml files I want to check_with_regex
        _r'\d{9}.xml' and r'\d{9}_\d.xml' """
    try:
        # needs a comprension
        check_file = re.search(regexstring, the_vila_ordernum_xml)

        if check_file.group() == the_vila_ordernum_xml:
            print(f'{check_file = }')
            # return output_regex_search
            return the_vila_ordernum_xml
        else:
            return None

    except AttributeError:
        print("AttributeError: no Match")
        return None


def pad_naar_item_nummer_folder_maker(voor_itemnummer_uit_lijst):
    """Builds a path filename from the vila item number for the
    Helloprint, Drukwerkdeal and print.com reseller clients.
    # hp_id = "806321"
    # dwd_id = "569621"
    # pdc_id = "935321
    """
    voor_itemnummer_uit_lijst = str(voor_itemnummer_uit_lijst)
    itemnummer_pdf = voor_itemnummer_uit_lijst + ".pdf"

    def foldername_based_on_itemnummer(itemnummer):
        itemnummer = str(itemnummer)
        folderbase = itemnummer[4:9]
        foldername = folderbase + "000-" + folderbase + "999"
        return foldername

    def klantnummer_uit(itemnummer):
        itemnummer = str(itemnummer)
        klantnummer = itemnummer[0:6]
        return klantnummer

    klant_naam_paden = [(WDIR_PRODUCTS_MAC_server.joinpath(name[0], name)) for name in klantnamen]
    # todo maak paden dynamisch met een dict bijvoorbeeld key is klantnaam
    helloprint_base_path = klant_naam_paden[0]
    drukwerkdeal_base_path = klant_naam_paden[1]
    print_dot_com_base_path = klant_naam_paden[2]
    vila_etiketten_path =  klant_naam_paden[3]
    distrifill_path = klant_naam_paden[4]

    foldername = foldername_based_on_itemnummer(voor_itemnummer_uit_lijst)

    match klantnummer_uit(voor_itemnummer_uit_lijst):
        case "806321":
            return Path(helloprint_base_path.joinpath(foldername, voor_itemnummer_uit_lijst, itemnummer_pdf))

        case "569621":
            return Path(drukwerkdeal_base_path.joinpath(foldername, voor_itemnummer_uit_lijst, itemnummer_pdf))

        case "935321":
            return Path(print_dot_com_base_path.joinpath(foldername, voor_itemnummer_uit_lijst, itemnummer_pdf))

        case "380321":
            return vila_etiketten_path.joinpath(foldername, voor_itemnummer_uit_lijst, itemnummer_pdf)

        case "982521":
            return Path(distrifill_path.joinpath(foldername, voor_itemnummer_uit_lijst, itemnummer_pdf))
