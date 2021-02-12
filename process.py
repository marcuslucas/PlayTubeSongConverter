import string

from converter import convert
from db import get_files


def fix_title(s):
    s2 = s.replace(" ", "-").replace("--", "").replace("|", "").replace('""', '').replace("@", "")
    exclude = set(string.punctuation)
    s3 = ''.join(ch for ch in s2 if ch not in exclude)
    printable = set(string.printable)
    s4 = ''.join(filter(lambda x: x in printable, s3))
    return s4

def process(db_file, input_dir, output_dir):
    rows = get_files(db_file)
    for row in rows:
        id = row[0]
        title = row[1]
        pos = row[2]
        new_title = fix_title(title)
        # print(id, pos, title, new_title)
        input_file = input_dir + "/" + id + ".mp4"
        output_file = output_dir + "/" + str(pos) + "-" + new_title + ".mp3"
        print(input_file, output_file)
        convert(input_file, output_file)


if __name__ == "__main__":
    input_dir = "data"
    output_dir = "output"
    db_file = "data/playTube.db"
    process(db_file, input_dir, output_dir)