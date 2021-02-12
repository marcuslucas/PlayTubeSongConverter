import string
from shutil import copyfile

input_dir2 = r"C:\Users\marcu\Desktop\data"
output_dir = r"C:\Users\marcu\Desktop\data_output"

def fix_title(s):

    s2 = s.replace(" ", "-").replace("--", "").replace("|", "").replace('""', '').replace("@", "")
    exclude = set(string.punctuation)
    s3 = ''.join(ch for ch in s2 if ch not in exclude)
    printable = set(string.printable)
    s4 = ''.join(filter(lambda x: x in printable, s3))
    return s4


def rename_file(id, title, pos):
    input_file = input_dir2 + "\\" + id + ".mp4"
    output_file = output_dir + "\\" + str(pos) + "-" + fix_title(title) +".mp4"
    # print(input_file)
    # print(output_file)
    # print("--")
    rtn = False
    try:
        copyfile(input_file, output_file)
        rtn = True
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)
    return rtn