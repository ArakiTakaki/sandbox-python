# -*- coding: utf-8 -*-
from datas import Store


# 色のフォーマット用Enum
class color:
    OK = '\033[92m'
    WARN = '\033[93m'
    NG = '\033[91m'
    END_CODE = '\033[0m'


# テストを実施するメソッド
# name='テストケースの識別名'
def expect(name, check):
    success = '{s}OK{e}'.format(s=color.OK, e=color.END_CODE)
    ng = '{s}NG{e}'.format(s=color.NG, e=color.END_CODE)
    tmp = None
    if check:
        tmp = '{name} : [ {command} ]'.format(name=name, command=success)
    else:
        tmp = '{name} : [ {command} ]'.format(name=name, command=ng)
    print(tmp)


testCase = 10
dumpStore = Store(name='test2', test=testCase)
dumpStore.dump()

# ストアが存在していた場合のテストケース
loadStore = Store.load(name='test2')
expect('Store load Test', loadStore.test == testCase)

# ストアのファイルが存在していない場合のテストケース
notStore = Store.load(name='test3')
expect('Not Exists Test', notStore == None)
