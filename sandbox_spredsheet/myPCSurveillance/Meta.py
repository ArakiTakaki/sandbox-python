import subprocess
import re


# @return { 'nowTime' 'uptime' 'users' 'loadAverages' 'nowDateTime' }
def getPCMetaData():
    data = []

    result = subprocess.check_output('uptime')
    result = shapingStr(result.decode('utf-8'))
    data.extend(result.split(','))

    cmd = 'date +%Y/%m/%d-%H:%M:%S'
    result = subprocess.check_output(cmd.split())
    result = shapingStr(result.decode('utf-8'))
    data.append(result)
    return data


def shapingStr(data):
    return data.replace('\n', '').replace(', ', ',')
