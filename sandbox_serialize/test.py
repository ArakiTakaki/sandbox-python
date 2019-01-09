import os
import json

"""
with構文は、closeを自動的に記載してくれる。
リソースの解放をワンライナーで記述できるので非常に便利。
"""

# ファイルの上書き
with open('sample.txt', mode='w', encoding='utf-8') as f:
    print(f.write('よろしくお願いいたします。\n'))

# ファイルの読み込み
with open('sample.txt', mode='r', encoding='utf-8') as f:
    print(f.read())

# ファイルの追記モード おそらくappendのa?
with open('sample.txt', mode='a', encoding='utf-8') as f:
    print(f.write('a\n'))

# 存在チェック
fileName = 'sample.txt'
if os.path.exists(fileName):
    print("{fileName}は存在しています".format(fileName=fileName))
# ファイルの削除を実行
os.remove(fileName)

# 再帰的にファイルを削除する。
# import shutil
# shutil.rmtree('data')

mock = {
    'test': 'aiueo',
    'sample': ['kakikukeko', 'sasisuseso']
}
serializeData = 'data.json'
# エンコード
with open(serializeData, mode='w', encoding='utf-8') as f:
    mock['test'] = 'dumpppp'
    sampleJsonDataText = json.dumps(mock)
    f.write(sampleJsonDataText)

# デコード
sampleJsonDataObject = json.loads(sampleJsonDataText)
print(sampleJsonDataObject['sample'])

tmp = None
with open(serializeData, mode='r', encoding='utf-8') as f:
    tmp = json.loads(f.read())

print(tmp)
