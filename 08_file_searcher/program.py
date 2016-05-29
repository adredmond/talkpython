import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')


def main():
    print_header()
    folder = get_folder()
    search_term = get_search_term()
    matches = search(folder, search_term)

    for match in matches:
        print('------------ MATCH --------------')
        print('File: ', match.file)
        print('Line: ', match.line)
        print('Text: ', match.text)
        print()


def print_header():
    print('------------------------------------')
    print('     FILE SEARCH APP')
    print('------------------------------------')
    print()


def get_folder():
    folder = input("Which folder would you like to search?")
    # TODO: input sanitation
    if not folder or not folder.strip():
        print("Cannot find: ", folder)
        return None
    if not os.path.isdir(folder):
        print("{} is not a folder".format(folder))
        return None
    return os.path.abspath(folder)


def get_search_term():
    # TODO: input sanitation
    search_term = input('What term would you like to search? [single word only]')
    if not search_term:
        print("We can't search for nothing!")
        return None
    return search_term


def search(folder, search_term):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search(full_item, search_term)
        else:
            yield from search_file(item, search_term)


def search_file(filename, search_term):
    line_num = 0

    with open(filename, 'r', encoding="utf-8") as fin:
        for line in fin:
            line_num += 1
            if line.lower().find(search_term) >= 0:
                match = SearchResult(filename, line_num, line.strip())
                yield match


if __name__ == '__main__':
    main()
