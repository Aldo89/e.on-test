# e.on

## Setup:

1. Python version 3.10
2. PyCharm Community Edition 2023.1.3


## Issues in the dataset:

1. The column `order_date` is a charcter column so I converted it to datetime.
2. In the column `postcode` the values are not just 5 digits.
   1. The strings appear to have float values like 74235.0 -> I replaced '.0' with ''
   2. There is a value in the column that contains non-digit values -> Replaced characters with empty string 
   3. There are postcodes that only have 4 digits and not 5 -> Padded them with a 0 in the front

3. In the column `bundesland` there are 29532 missing values.
   1. 1543 postcode entries have either an entry in `bundesland` and also an empty one. -> Filled them with other value
   2. 3 postcode entries have multiple values (more than 2) in the column `bundesland`. -> Deleted them as they can not be assigned to one `bundesland`
   3. 676 postcode do not have a value in `bundesland`.
 
## Execute code:
Execute `data_transformation.py`