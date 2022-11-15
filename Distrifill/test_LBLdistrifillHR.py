from Distrifill.LBLdistrifillHR import rename_only_distrifill


def test_rename_only_distrifill():
    itemnummer1 = 982521000001  # distrifill
    itemnummer2 = 806321000001  # helloprint
    test = rename_only_distrifill(1234567,itemnummer1)
    result = '806321'
    result2 = "LBL_1234567_HR_1"


    assert test == result2
