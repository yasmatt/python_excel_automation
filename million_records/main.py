import pandas as pd

if '__main__' == __name__:
    # エクセルファイル名
    output_xls = 'sales_data_m.xlsx'

    # エクセルファイルを読み込む
    sales_data_raw = pd.read_excel(output_xls)

    # 顧客別に売上を集計
    sales_data_by_company = sales_data_raw.groupby(['企業名']).sum()

    # 顧客ｘ日付別で売上を集計
    sales_data_by_company_date = sales_data_raw.groupby(['企業名', '日付']).sum()

    # 結果を出力
    with pd.ExcelWriter('results.xlsx') as writer:
        sales_data_by_company.to_excel(writer, sheet_name='売上実績_顧客別')
        sales_data_by_company_date.to_excel(writer, sheet_name='売上実績_顧客ｘ日付別')
