from DataProcessor import DataProcessor

# File path
file_path = 'interview_signup.csv.gz'

# Create an instance of DataProcessor
processor = DataProcessor(file_path)

# Perform data preprocessing
processor.preprocess_data()

# Access the preprocessed data
preprocessed_data = processor.data

# Perform further operations on preprocessed_data as needed
# For example, you can print the first few rows:
print(preprocessed_data)
