from content.sheets import Sample
from myLib.google.spredAPI import getSheet

# Sheetの名前とページを選択？
wks = getSheet(Sample.SHEET_NAME).sheet1

# 書き込み
wks.update_acell(Sample.cpu(1), 'CPU')
wks.update_acell(Sample.memory(1), 'MEMORY')
print(wks.acell('A2'))
