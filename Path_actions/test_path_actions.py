from pathlib import Path
from unittest import TestCase

from .path_actions import find_, WDIR_Job, check_with_regex, pad_naar_item_nummer_folder_maker


def test_find_():
    test = find_(WDIR_Job, 100)
    result = [('a', 'b')]

    assert test == result


regexstring_vilaorder = r'\d{9}.xml'
regexstring_vilaitem = r'\d{9}_\d.xml'


def test_check_with_regex():
    vila = "202212345.xml"
    item = "202212345_1.xml"
    test = check_with_regex(vila, regexstring_vilaorder)
    test2 = check_with_regex(item, regexstring_vilaitem)

    assert test2 == True


def test_pad_naar_item_nummer_folder_maker():
    itemnummer1=982521000001    # distrifill
    itemnummer2=806321000001    # helloprint

    test = pad_naar_item_nummer_folder_maker(itemnummer1)
    result = Path('/Volumes/Afdeling prepress/ESKO/Products/D/Distrifill/21000000-21000999/982521000001/982521000001.pdf')
    assert test == result
