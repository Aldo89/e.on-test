import pandas as pd

class DataProcessor:
    """
    Class to process signup data with columns original_product_name, postcode, bundesland, total_bonus and order_date.
    """
    def __init__(self, file_path):
        """
        :param file_path: filepath of datain .csv.gz format
        """
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
        """
        Remove decimal point from postcode values.
        :return: None
        """
        self.data['postcode'] = self.data['postcode'].astype('str')
        self.data['postcode'] = self.data['postcode'].str.replace(r'.0', '')

    def remove_non_digit_postcode_entries(self):
        self.data['postcode'] = self.data['postcode'].str.replace(r'\D', '', regex=True)

    def fill_postcode_length(self):
        self.data['postcode'] = self.data.postcode.astype(str).str.pad(5, fillchar='0')

    def drop_duplicate_combinations(self):
        """
        Determine duplicate combinations of postcode and bundeland. Drop these that have more than 3 combinations.
        :return: None
        """
        post_bund = self.data.loc[:, ['postcode', 'bundesland']]
        post_bund_unq = post_bund.drop_duplicates()
        post_bund_unq['cnt'] = post_bund_unq.groupby(['postcode'])['postcode'].transform('count')
        self.data = self.data.merge(post_bund_unq)
        self.data = self.data[self.data.cnt < 3]
        self.data = self.data.drop(columns='cnt')

    def fill_missing_bundesland(self):
        """
        Fill the missing values in the postcodes that have a combination of 2.
        :return: data
        """
        self.data = self.data.sort_values(['postcode', 'bundesland'], ascending=[True, False])
        self.data['key'] = self.data['postcode']
        self.data = self.data.groupby('key').fillna(method="ffill")
        return(self.data)
