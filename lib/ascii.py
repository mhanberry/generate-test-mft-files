from faker import Faker
from lib.util import print_progress

def gen_files(
    sizes_mb: int = [100, 3700, 5000],
    num_cards: int = 100000,
    card_types: list[str] = ['mastercard', 'visa'],
    region: str = 'en_US',
    output_dir: str = 'output'
) -> None:
    '''
        Generates simulated ASCII user files and saves them in the `output` directory
        
        sizes_mb: int
            The sizes of files to generate in megabytes
        num_cards: int
            The number of different cards records to generate for each card type
        card_types: list[str]
            The card types to generate records for
        region: str
            The geographic region to simulate records for
        
        return: None
    '''
    
    faker = Faker(region)
    total_lines = len(card_types) * num_cards
    lines = []

    # Generate lines to use in the output files
    for card_type in card_types:
        for _ in range(num_cards):
            number = faker.credit_card_number(card_type=card_type)
            exp_date = faker.credit_card_expire()
            name = faker.name()
            
            lines.append('{number},{exp_date},{name}\n')

            # Print progress
            print_progress('    Generating data...', len(lines), total_lines)
    print()

    # Create output files of each size
    for size in sizes_mb:
        file_name = f'{output_dir}/ascii_{size}'
        output_file = open(file_name, 'w')
        line_size = len(lines[0])
        size_in_bytes = size * 1000000
        current_size = 0
        
        # Keep writing lines until the desired size is reached
        while(current_size < size_in_bytes):
            for line in lines:
                output_file.write(line)
                current_size += line_size
        
                # Print progress
                print_progress(f'    {file_name}...', current_size, size_in_bytes)
        
                if current_size > size_in_bytes:
                    break
        print()
