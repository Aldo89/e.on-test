# Explorative data analysis
## Import libraries
import pandas as pd

## Read data
data = pd.read_csv('interview_signup.csv.gz', compression='gzip')

## Get data types
print(data.info())

## Print first 5 rows
print(data.head())

## Detect non-digit values
data['postcode'] = data['postcode'].astype('str')
non_digit_values = data[data['postcode'].str.contains('[a-zA-Z]')]
print(non_digit_values)


## Detect length of postcode entries
data['postcode'] = data['postcode'].str.replace(r'.0', '')
data['postcode'] = data['postcode'].str.replace(r'\D', '', regex=True)
string_lengths = data['postcode'].str.len()

# Calculate the maximum and minimum string lengths
maximum_length = string_lengths.max()
minimum_length = string_lengths.min()

# Print the maximum and minimum lengths
print("Maximum length:", maximum_length)
print("Minimum length:", minimum_length)

# Count the number of missing values in each column
missing_values_count = data.isnull().sum()

# Print the number of missing values for each column
print(missing_values_count)

# Detect duplicat combinations between postcode and bundesland
post_bund = data.loc[:, ['postcode', 'bundesland']]
post_bund_unq = post_bund.drop_duplicates()
post_bund_unq['cnt'] = post_bund_unq.groupby(['postcode'])['postcode'].transform('count')
print(post_bund_unq)