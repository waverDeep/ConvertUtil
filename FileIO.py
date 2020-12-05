import os
import glob
import natsort
import csv
import json


# find all dataset filepath
def get_all_file_path(input_dir, file_extension):
    temp = glob.glob(os.path.join(input_dir, '**', '*.{}'.format(file_extension)), recursive=True)
    return temp


def open_file(file_path):
    f = open(file_path)
    return f


def get_pure_filepath(filename):
    temp = filename.split('/')
    del temp[-1]
    temp = '/'.join(temp)
    return temp


def get_pure_filename(filename):
    temp = filename.split('.')
    del temp[-1]
    temp = ' '.join(temp)
    temp = temp.split('/')
    temp = temp[-1]
    return temp


def read_txt_file(file_path, encoding='utf8'):
    lines = []
    f = open(file_path, 'r', encoding=encoding, errors='ignore')
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)
    f.close()
    return lines


def read_text_file_one_line(file_path, encoding='utf8'):
    f = open(file_path, 'r', encoding=encoding)
    line = f.readline()
    f.close()
    line = line.replace('\n', '')
    return line


# by kspon
def get_divided_script(input_dir, file_extension='txt'):
    temp = get_all_file_path(input_dir, file_extension)
    temp = natsort.natsorted(temp)
    return temp


def filename_script_pair_tolist(filename, encoding):
    line = read_text_file_one_line(filename, encoding)
    pure_filename = get_pure_filename(filename)
    temp = [pure_filename, line]
    return temp


def write_csv_file(dataset, filepath, filename, divider=' ', encoding='utf8'):
    file = open('{}/{}'.format(filepath, filename), 'w', encoding=encoding)
    wr = csv.writer(file, delimiter=divider)
    for data in dataset:
        wr.writerow(data)
    file.close()


def read_csv_file(filepath, filename, encoding='utf-8', divider=' '):
    file = open('{}/{}'.format(filepath, filename), 'r', encoding=encoding)
    rdr = csv.reader(file, delimiter=divider)
    for line in rdr:
        print(line)
    file.close()


def write_label(filepath, filename, label_list):
    f = open("{}/{}".format(filepath, filename), 'w', encoding='utf8')
    for label in label_list:
        f.write('{}\n'.format(label))
    f.close()


def write_json_file(dataset, filepath, encoding='utf8'):
    with open(filepath, 'w', encoding=encoding) as file:
        file.write(json.dumps(dataset, ensure_ascii=False))
    # with open(filepath, 'w', encoding=encoding) as outfile:
    #     json.dump(dataset, outfile)


def read_json_file(filepath, encoding='utf8'):
    with open(filepath) as json_file:
        json_data = json.load(json_file)
    return json_data


def convert_filename(original_filename, new_filename):
    os.rename(original_filename, new_filename)

