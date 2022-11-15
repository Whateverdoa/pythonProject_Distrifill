import shutil


def gebruik_shutill_en_verplaats_file_van(tuple_original_pad_and_destination_pad):
    """simple function for moving and renaming files """
    try:
        original_pad, destination_pad = tuple_original_pad_and_destination_pad
        shutil.copyfile(original_pad, destination_pad)

    except OSError as e:
        print(e)

    return original_pad, destination_pad


def distrifill_rename(item_string_CustomerProductReference):
    """this is a custom-made function to rename a 'CustomerProductReference'
    so we are able to find the right itemnumber.
     if we need to generalise the function
     #todo there should be a check on client number to NOT change anything"""
    item_string_CustomerProductReference = str(item_string_CustomerProductReference)

    if item_string_CustomerProductReference[-2:] == "/b":
        back = "LBL_" + item_string_CustomerProductReference.replace("/b", "_HR_2")
        return back
    elif item_string_CustomerProductReference[-2:] == "/f":
        front = "LBL_" + item_string_CustomerProductReference.replace("/f", "_HR_1")
        return front
    else:
        backfront = "LBL_" + item_string_CustomerProductReference + "_HR_1"
        return backfront


def rename_only_distrifill(item_string_CustomerProductReference, itemnumber):
    """look at customernumber to walk through tree"""
    itemnumber = str(itemnumber)[0:6]
    if itemnumber != "982521":
        return item_string_CustomerProductReference
    else:
        return distrifill_rename(item_string_CustomerProductReference)


if __name__ == "__main__":
    a = '001410810/b'
    b = '001410810/f'
    c = '001410810'
    print(distrifill_rename(a))
    print(distrifill_rename(b))
    print(distrifill_rename(c))
