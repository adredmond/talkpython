import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------------')
    print('    JOURNAL APP')
    print('--------------------------')


def run_event_loop():
    print('What would you like to do with your journal?')

    journal_name = 'default'
    journal_data = journal.load(journal_name)
    cmd = 'EMPTY'

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it:  ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmdw:
            print("Sorry, I don't understand '{}'".format(cmd))

    journal.save(journal_name, journal_data)
    print('Goodbye')


def list_entries(data):
    print('Your journal entries')
    for idx, entry in enumerate(data):
        print('Entry {}: {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('What would you like to enter? <enter> for exit  ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
