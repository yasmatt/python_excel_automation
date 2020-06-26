from  data_generator.generator import generate_romdom_dataset
from  data_generator.xls import create_xls_from_csv


if '__main__' == __name__:
    output_csv = 'sales_data.csv'
    output_xls = 'sales_data.xlsx'
    sheet_name = '売上実績'
    generate_romdom_dataset(output_csv, num_rows=1000)
    create_xls_from_csv(sheet_name, output_csv, output_xls)
