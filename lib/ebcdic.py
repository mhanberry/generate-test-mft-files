import os
from lib.util import print_progress

def conv_ascii_files(
    output_dir: str = 'output'
) -> None:
    '''
        Converts ascii test files to ebcdic
    
        output_dir: str
            The directory in which the generated files will be stored
        
        return: None
    '''

    output_files = os.listdir(output_dir)
    ascii_filenames = list(filter(lambda filename: filename[0:5] == 'ascii', output_files))
    ascii_filenames.sort()

    for ascii_filename in ascii_filenames:
        ebcdic_filename = ascii_filename.replace('ascii', 'ebcdic')
        in_file = open(f'{output_dir}/{ascii_filename}', 'r')
        out_file = open(f'{output_dir}/{ebcdic_filename}', 'wb')
        total_bytes = os.path.getsize(f'{output_dir}/{ascii_filename}')
        current_bytes = 0
        
        for line in in_file:
            current_bytes += len(line)
            out_file.write(line.encode('cp037'))
            print_progress(f'    {ebcdic_filename}...', current_bytes, total_bytes)
        
        print()
