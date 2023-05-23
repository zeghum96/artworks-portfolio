# artworks-portfolio
This repository contains a script for cleaning and processing an artworks dataset, preparing it for use in a portfolio or for client presentations. The script performs various data cleaning tasks, including handling missing values, formatting dates, and removing bad characters.
# Usage
Clone the repository:
git clone https://github.com/zeghum96/artworks-portfolio.git
Install the required dependencies:
Place the original artworks dataset (artworks.csv) in the repository directory.
Run the script:
python clean_artworks.py
The cleaned dataset (artworks_clean.csv) will be generated in the repository directory.
# Script Details
`*` The script cleans the nationality and gender columns, handling parentheses and formatting the values.
`*` It converts birth and death dates to a consistent format and handles missing values.
`*` The script removes bad characters from the date column, including spaces, quotes, parentheses, dots, and other characters.
`*` Date ranges are split and the average is calculated for the artwork creation date.
`*` The cleaned dataset is written to a new CSV file (artworks_clean.csv).
Feel free to explore the script and customize it according to your specific requirements.
