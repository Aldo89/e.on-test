import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, compression='gzip')

    def preprocess_data(self):
        self.convert_to_date()
        self.remove_postcode_decimal()
        self.remove_non_digit_postcode_entries()
        self.fill_postcode_length()
        self.drop_duplicate_combinations()
        self.fill_missing_bundesland()

    def convert_to_date(self):
        self.data['order_date'] = pd.to_datetime(self.data['order_date'])

    def remove_postcode_decimal(self):
        self.data['postcode'] = self.data['postcode'].astype('str')
        self.data['postcode'] = self.data['postcode'].str.replace(r'.0', '')

    def remove_non_digit_postcode_entries(self):
        self.data['postcode'] = self.data['postcode'].str.replace(r'\D', '', regex=True)

    def fill_postcode_length(self):
        self.data['postcode'] = self.data.postcode.astype(str).str.pad(5, fillchar='0')

    def drop_duplicate_combinations(self):
        post_bund = self.data.loc[:, ['postcode', 'bundesland']]
        post_bund_unq = post_bund.drop_duplicates()
        post_bund_unq['cnt'] = post_bund_unq.groupby(['postcode'])['postcode'].transform('count')
        self.data = self.data.merge(post_bund_unq)
        self.data = self.data[self.data.cnt < 3]
        self.data = self.data.drop(columns='cnt')

    def fill_missing_bundesland(self):
        self.data = self.data.sort_values(['postcode', 'bundesland'], ascending=[True, False])
        self.data['key'] = self.data['postcode']
        self.data = self.data.groupby('key').fillna(method="ffill")
        return(self.data)
