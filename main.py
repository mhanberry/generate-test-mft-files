from lib import ascii

def main():
    print('Generating ascii files...')

    ascii.gen_files()

    print('Done.')
    print('The generated files can be found in the `output` directory')

if __name__ == '__main__':
    try:
        print('\033[?25l', end="") # Hide terminal the cursor
        main()
    finally:
        print('\033[?25h') # Show termial the cursor
