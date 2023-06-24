# Import libraries
import pandas as pd

# Read data
data = pd.read_csv('data/interview_signup.csv.gz', compression='gzip')

# Date is a charecter and we coescre it to date.
data['order_date'] = pd.to_datetime(data['order_date'])

# In the head I see that the postcode have .0 values. I will delete them
data['postcode'] = data['postcode'].astype('str')
data['postcode'] = data['postcode'].str.replace(r'.0','')

# Column postcode can not be coerced into int because it contains values other than digits. So I delete the entries with
# non-digit values.
data['postcode_is_digit'] = list(map(lambda x: x.isdigit(), data['postcode']))
cnt_false = data['postcode_is_digit'].value_counts()

data.loc[data['postcode_is_digit'] == False, 'postcode'] = None

# Remove column postcode_is_digit
data = data.drop(columns='postcode_is_digit')

# Find missing data


# Drop rows where postcode and bundesland are missing
data = data.drop(data[(data['postcode'].isnull()) & (data['bundesland'].isnull())].index)

# Fill postcodes with the legth of 4 with a 0 in front to get legth 5.
data['postcode'] = data.postcode.astype(str).str.pad(5,fillchar='0')

# Fill missing values
data = data.sort_values(['postcode', 'bundesland'], ascending=[True, False])
data['key'] = data['postcode']
data = data.groupby('key').fillna(method="ffill")



