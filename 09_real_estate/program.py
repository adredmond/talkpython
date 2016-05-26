import os


def main():
    print_header()
    filename = get_data_file()
    data = load_data(filename)
    query_data(data)


def print_header():
    print('------------------------------------')
    print('       REAL ESTATE APP')
    print('------------------------------------')
    print()


def get_data_file():
    basedir = os.path.basename(__file__)
    return os.path.join(basedir, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_data(filename):
    return []


def query_data(data):
    print('data goes here')


if __name__ == '__main__':
    main()
