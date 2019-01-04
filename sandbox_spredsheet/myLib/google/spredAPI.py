import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# シートのAPIを取得する
def getSheet(name):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'key.json', scope)
    gc = gspread.authorize(credentials)
    return gc.open(name)
