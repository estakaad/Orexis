import gspread
from oauth2client.service_account import ServiceAccountCredentials
from configparser import ConfigParser


config_parser = ConfigParser()
config_parser.read('config.ini')

def create_client():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    return gspread.authorize(creds)


#Writing results to the spreadsheet. Column A is date, B is for kcal consumed and C is for kcal burned.
def write_kcal_to_sheet(client, nutri_kcal, endo_kcal, date):
    sheet_name = config_parser.get('Google API', 'sheetname')
    sheet = client.open(sheet_name).sheet1
    cell_list = sheet.findall(date)

    date_cell_row = cell_list[0].row
    sheet.update_acell('B' + str(date_cell_row), nutri_kcal)
    sheet.update_acell('C' + str(date_cell_row), endo_kcal)