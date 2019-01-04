import subprocess
import os
"""
UNIXシェルコマンドを起動するPythonコマンド
"""

# macに対して通知を行う
def pushForMac(title, subtitle, notification):
    display = "osascript -e ' display notification \"{notification}\" with title \"{title}\" subtitle \"{subtitle}\" '".format(
        title=title, subtitle=subtitle, notification=notification)
    return os.system(display)


# subprocess.call(script)
# subprocess.check_output(script)
# res = subprocess.check_output('pwd')
# print(res)
# => lsコマンドの結果
# => コマンドが成功していれば 0
