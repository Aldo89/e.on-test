# e.on

Issues in the dataset:

1. The column order_date is a charcter column so I converted it to datetime.
2. In the column postcode the values are not just 5 digits.
   1. The strings appear to have float values like 80687.0
   2. There is a value in the column that contains non-digit values
   3. There are postcodes that only have 4 digits and not 5

3. In the column bundesland there are 29532 missing values. I fill it with 
 
