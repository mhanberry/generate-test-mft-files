from faker import Faker

def gen_files(
    num_files: int = 3,
    num_cards: int = 100000,
    card_types: list[str] = ['mastercard', 'visa'],
    region: str = 'en_US',
    output_dir: str = 'output'
) -> None:
    '''
        Generates simulated ASCII user files and saves them in the `output` directory
        
        num_files: int
            The number of files to generate
        num_cards: int
            The number of different cards records to generate for each card type
        card_types: list[str]
            The card types to generate records for
        region: str
            The geographic region to simulate records for
        
        return: None
    '''
    
    faker = Faker(region)
    
    for i in range(num_files):
        file_name = f'{output_dir}/ascii_{i}'
        output_file = open(file_name, 'w')
        
        print(f'{file_name}...')
        
        for card_type in card_types:
            for _ in range(num_cards):
                number = faker.credit_card_number(card_type=card_type)
                exp_date = faker.credit_card_expire()
                name = faker.name()
                
                output_file.write(f'{number},{exp_date},{name}\n')
