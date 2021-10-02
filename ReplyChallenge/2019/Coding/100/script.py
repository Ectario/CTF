#!/usr/bin/env python3

FILE_NAME = "2c464e58-9121-11e9-aec5-34415dec71f2.txt"
OUTPUT_NAME = "output.txt"

def main():
    with open(FILE_NAME,'r') as FILE:
        new_file = FILE.read()

        new_file = new_file.replace('#','')

        with open(OUTPUT_NAME, 'w') as NEW_FILE:
            NEW_FILE.write(new_file)

if __name__ == '__main__':
    main()