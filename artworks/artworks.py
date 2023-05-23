from csv import reader, writer

def clean_and_convert(date):
    if date != '':
        date = date.replace('-', '')
        date = int(date)
    return date

def remove_bad_characters(string):
    bad_characters = [' ', "'", '(', ')', '-', '.', 'c', 's']
    for char in bad_characters:
        string = string.replace(char, '')
    return string

def split_and_average(string):
    if '-' in string:
        first_index, second_index = map(int, string.split('-'))
        avg = round((first_index + second_index) / 2)
        string = str(avg)
    return string

# Read the input CSV file
with open('artworks.csv', encoding='utf-8') as opened_file:
    read_file = reader(opened_file)
    dataset = list(read_file)

# Extract the header and remove it from the dataset
header = dataset[0]
dataset = dataset[1:]

# Clean the nationality and gender columns
for i in dataset:
    nationality = i[2].replace('(', '').replace(')', '')
    i[2] = nationality

for i in dataset:
    gender = i[5].replace('(', '').replace(')', '')
    i[5] = gender.title() if gender else 'Gender Unknown/Others'

# Clean and convert birth and death dates
for i in dataset:
    birth_date = i[3]
    death_date = i[4]
    birth_date = clean_and_convert(birth_date)
    death_date = clean_and_convert(death_date)
    i[3] = birth_date
    i[4] = death_date

# Identify and remove bad characters
for i in dataset:
    date = remove_bad_characters(i[6])
    i[6] = date

# Split date ranges and calculate average
for i in dataset:
    if '-' in i[6]:
        date = split_and_average(i[6])
        i[6] = int(date)

# Write the cleaned dataset to a new CSV file
with open('artworks_clean.csv', 'w', newline='\n', encoding='utf-8') as f:
    csv_writer = writer(f, delimiter=',')
    csv_writer.writerow(header)
    csv_writer.writerows(dataset)