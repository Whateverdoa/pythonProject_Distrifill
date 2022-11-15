#!/usr/bin/python3.11
# -*- coding: utf8 -*-
from pathlib import Path
import PySimpleGUI as sg
import pandas as pd
import sys

# from Distrifill.LBLdistrifillHR import gebruik_shutill_en_verplaats_file_van
from Distrifill.distrifill_itemnummer import customernum, Mnumber, item_number, distrifill_item_rename, tuple_destinies
from Path_actions.pad_namen import PDF_bestanden_map
from Path_actions.path_actions import check_with_regex, regexstring_vilaitem

def main():
    sg.ChangeLookAndFeel('BlueMono')



    if len(sys.argv) == 1:
        fname = sg.popup_get_folder('FOLDER CONTAINING 2022xxxxx_1.XML')
    else:
        fname = sys.argv[1]

    if not fname:
        sg.popup("Cancel", "No filename supplied")
        raise SystemExit("Cancelling: no filename supplied")
    else:
        # sg.popup('The filename you chose was', fname)
        pad = Path(fname)
        print(f"volledig pad: {pad = }")

        glob_dwd_pdf = sorted(PDF_bestanden_map.rglob("*.pdf"))
        vila_xml = sorted(pad.rglob("*.xml"))
        print(vila_xml)
        vila_1_xmls_are = [(check_with_regex(str(xml.name),regexstring_vilaitem),xml) for xml in vila_xml
                           if check_with_regex(str(xml.name),regexstring_vilaitem) != None]
        vila_1_xmls = [xml.name for xml in vila_xml]
        print(vila_1_xmls_are)
        print(vila_1_xmls)

        customernumbers = [(customernum(padxml[1]), Mnumber(padxml[1]), item_number(padxml[1]), padxml[1]) for padxml in vila_1_xmls_are]

        customernum_dict = {f'{distrifill_item_rename(Mnumber(padxml[1]))}': (distrifill_item_rename(Mnumber(padxml[1])), item_number(padxml[1]), padxml[1]) for padxml in vila_1_xmls_are}
        #
        # Mbestandsnaam = [bestandsnaam.stem for bestandsnaam in glob_dwd_pdf]
        #
        two_tuple_pair_list = [tuple_destinies(pad,customernum_dict,key) for key in customernum_dict]
        for lijst in two_tuple_pair_list:
            print(lijst)

        # moves the files to a collecting folder for easy insertion in labelhub
        # and one that places them in esko.
        #
        # moving = [(gebruik_shutill_en_verplaats_file_van(tuplelist[0]),
        #            gebruik_shutill_en_verplaats_file_van(tuplelist[1]))
        #           for tuplelist in two_tuple_pair_list]

if __name__ == '__main__':
    main()
