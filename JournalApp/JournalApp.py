#!/usr/bin/env python
# coding: utf-8

import journalBackend


def main():
    print_header()
    run_event_loop()
    

def print_header():
    print('----------------------')
    print('-------JOURNAL--------')
    print('----------------------')
    

def run_event_loop():
    print('What do you want to do in your journal?')
    cmd = 'Empty'
    journal_name = 'default'
    journal_data = journalBackend.load(journal_name)
    
    while cmd != 'x' and cmd:
        cmd = input("[L]ist entries, [A]dd entries, e[X]it : ")
        cmd = cmd.lower().strip()
        
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry we don't understand '{}'".format(cmd))
            
    print('Done, Goodbye then.')
    journalBackend.save(journal_name, journal_data)

    
    
def list_entries(data):
    print("Listing...")
    print('Your journal entries : ')
    entries = reversed(data)
    
    for idx, entry in enumerate(entries):
        print("* {}) {}".format(idx+ 1,entry))
    
    
def add_entries(data):
    print("Adding...")
    text = input("Type what you want to add to your journal, press enter when done : ")
    journalBackend.add_entry(text, data)
    


if __name__ == '__main__':
    main()





