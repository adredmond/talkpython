import os


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def load(name):
    filename = get_full_pathname(name)
    data = []

    if os.path.exists(filename):
        print(' ... loading from {}'.format(filename))
        with open(filename) as fin:
            for line in fin.readlines():
                data.append(line.rstrip())
    return data


def save(name, data):
    filename = get_full_pathname(name)
    print(' ... saving to {}'.format(filename))
    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def add_entry(text, data):
    data.append(text)
