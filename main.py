from lib import ascii

def main():
    print('Generating ascii files...')

    ascii.gen_files(num_files=3)

    print('Done.')
    print('The generated files can be found in the `output` directory')

if __name__ == '__main__':
    main()
