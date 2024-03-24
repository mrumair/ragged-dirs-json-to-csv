## Find json files from ragged directory and convert to csv

This Python script converts JSON files located in a directory to CSV format. It flattens out nested JSON structures using Pandas and exports the flattened data to CSV files.

### Approach

1. **Finding JSON Files:**
   - The script uses the `glob` module to search for `JSON` files within a directory and its subdirectories.

2. **Loading JSON Files:**
   - Once the JSON files are located, they are loaded into memory using Python's built-in JSON module.

3. **Flattening Nested Structures:**
   - The loaded JSON data is then `flattened` out to a tabular format using Pandas DataFrame. This process involves converting nested JSON structures into a flat representation suitable for CSV conversion.

4. **Exporting to CSV:**
   - After flattening the data, it is exported to `CSV` format using Pandas DataFrame's to_csv method.
