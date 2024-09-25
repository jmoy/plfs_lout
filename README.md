Convert text microdata files from India's NSSO to CSV. Python script.

The script can parse the data layout Excel files provided by NSSO to get column names and widths.

I've only tested it for two rounds of PLFS. Your mileage may vary.

    Usage: python src/main.py [Data layout Excel file] [Input TXT file] [Output CSV file]

For eg.

    python src/main.py examples/Data_LayoutPLFS_2023-24.xlsx HHRV.TXT hhrv.csv
    
The script uses the input filename to select the field descriptions from the Excel layout file provided by NSSO, so the input filename should be unchanged.

You have to install the openpyxl package.
