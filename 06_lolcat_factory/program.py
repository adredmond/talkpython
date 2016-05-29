import os
import platform

import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('-------------------------------')
    print('         CAT FACTORY')
    print('-------------------------------')
    print()


def get_or_create_folder():
    folder_name = 'cat_pictures'
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, folder_name)

    if not os.path.exists(fullpath) and not os.path.isdir(fullpath):
        print('Creating directory at {}'.format(fullpath))
        os.mkdir(fullpath)

    return fullpath


def download_cats(folder):
    CAT_COUNT = 10
    print('Contacting server to download.')
    for cat in range(1, CAT_COUNT + 1):
        name = 'lolcat_{}'.format(cat)
        print('Downloading ' + name)
        cat_service.get_cat(folder, name)
    print('done')

def display_cats(folder):
    print('Display downloaded cats')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('Unable to launch display for ' + platform.system())
        print('Please find the cat pictures at ' + folder)

if __name__ == '__main__':
    main()
