from content.sheets import Sample
from myLib.google.spredAPI import getSheet
from myPCSurveillance import Meta
from time import sleep

# Sheetの名前とページを選択？
wks = getSheet(Sample.SHEET_NAME).sheet1

# 書き込み
# wks.update_acell(Sample.nowTime(1), 'TIME')
# wks.update_acell(Sample.uptime(1), 'UPTIME')
# wks.update_acell(Sample.users(1), 'USERS')
# wks.update_acell(Sample.loadAverage(1), 'LOAD AVERAGE')
# wks.update_acell(Sample.nowDateTime(1), 'DATE TIME')

data_list = Meta.getPCMetaData()
cell_list = wks.range('A{num}:E{num}'.format(num=2))
for idx in range(len(data_list)):
    cell_list[idx].value = data_list[idx]
wks.update_cells(cell_list)
