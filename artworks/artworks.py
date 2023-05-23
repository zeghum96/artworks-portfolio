from csv import reader, writer

# Read the input CSV file
opened_file = open('artworks.csv', encoding='utf-8')
read_file = reader(opened_file)
dataset = list(read_file)

# Extract the header and remove it from the dataset
header = dataset[0]
dataset = dataset[1:]

# Clean the nationality column
for i in dataset:
    nationality = i[2]
    nationality = nationality.replace('(', '')
    nationality = nationality.replace(')', '')
    i[2] = nationality

# Clean the gender column
for i in dataset:
    Gender = i[5]
    Gender = Gender.replace('(', '')
    Gender = Gender.replace(')', '')
    i[5] = Gender

# Title-case the gender column and handle missing values
for i in dataset:
    gender = i[5]
    gender = gender.title()
    if gender == "":
        gender = 'Gender Unknown/Others'
    i[5] = gender

# Title-case the nationality column and handle missing values
for i in dataset:
    nationality = i[2]
    nationality = nationality.title()
    if nationality != "":
        nationality.replace('', 'Gender Unknown/Others')
    i[2] = nationality

# Clean and convert birth and death dates
def clean_and_convert(date):
    if date != '':
        date = date.replace('-', '')
        date = int(date)
    return date

for i in dataset:
    birth_date = i[3]
    death_date = i[4]
    birth_date = clean_and_convert(birth_date)
    death_date = clean_and_convert(death_date)
    i[3] = birth_date
    i[4] = death_date

# Identify bad characters
bad_characters = []
for i in dataset:
    for j in i[-2]:
        try:
            int(j)
        except:
            bad_characters.append(j)

bad_characters = [' ', "'", '(', ')', '-', '.', 'c', 's']

# Remove bad characters from the date column
def bad_charac(string):
    bad_characters = [' ', "'", '(', ')', '.', 'c', 's']
    for i in bad_characters:
        string = string.replace(i, '')
    return string

# Remove leading hyphen from date column
def start_with_hyphen(string):
    if string.startswith('-'):
        string = string.replace('-', '')
    return string

for i in dataset:
    date = i[6]
    date = start_with_hyphen(date)
    i[6] = date

for i in dataset:
    date = i[6]
    date = bad_charac(date)
    i[6] = date

# Split date ranges and calculate averages
def split(string):
    if '-' in string:
        first_index = int(string.split('-')[0])
        second_index = int(string.split('-')[1])
        avg = round((first_index + second_index) / 2)
        string = str(avg)
    else:
        string = int(avg)
    return string

for i in dataset:
    if '-' in i[6]:
        date = split(i[6])
        i[6] = int(date)

# Write the cleaned dataset to a new CSV file
with open('artworks_clean.csv', 'w', newline='\n', encoding='utf-8') as f:
    csv_writer = writer(f, delimiter=',')
    csv_writer.writerow(header)
    csv_writer.writerows(dataset)
