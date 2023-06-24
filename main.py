# Import libraries
import pandas as pd

# Read data
data = pd.read_csv('data/interview_signup.csv.gz', nrows=100, compression='gzip')
print(data.head(10))

