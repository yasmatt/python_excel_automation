import pandas as pd

if '__main__' == __name__:
    output_xls = 'sales_data_m.xlsx'
    result_xls = 'result.xlsx'

    # read excel
    sales_data_raw = pd.read_excel(output_xls)

    # grope by compnay name
    sales_data_by_company = sales_data_raw.groupby(['企業名']).sum()
    
    # grope by compnay name and date
    sales_data_by_company_date = sales_data_raw.groupby(['企業名', '日付']).sum()

    # output result
    with pd.ExcelWriter(result_xls) as writer:
        sales_data_by_company.to_excel(writer, sheet_name='売上実績_顧客別')
        sales_data_by_company_date.to_excel(writer, sheet_name='売上実績_顧客ｘ日付別')
