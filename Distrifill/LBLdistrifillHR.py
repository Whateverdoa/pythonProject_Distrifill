import shutil


def gebruik_shutill_en_verplaats_file_van(tuple_original_pad_and_destination_pad):
    """simple function for moving and renaming files """
    try:
        original_pad, destination_pad = tuple_original_pad_and_destination_pad
        shutil.copyfile(original_pad, destination_pad)

    except OSError as e:
        print(e)

    return original_pad, destination_pad


def distrifill_item_rename(item_string):
    """this is a custom-made function to rename a 'CustomerProductReference'
    so we are able to find the right itemnumber.
     if we need to generalise the function
     #todo there should be a check on client number to NOT change anything"""

    if item_string[-2:] == "/b":
        back = "lBL_" + item_string.replace("/b", "_HR_2")
        return back
    elif item_string[-2:] == "/f":
        front = "lBL_" + item_string.replace("/f", "_HR_1")
        return front
    else:
        backfront = "lBL_" + item_string + "_HR_1"
        return backfront


if __name__ == "__main__":
    a = '001410810/b'
    b = '001410810/f'
    c = '001410810'
    print(distrifill_item_rename(a))
    print(distrifill_item_rename(b))
    print(distrifill_item_rename(c))
