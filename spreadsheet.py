import gspread
from oauth2client.service_account import ServiceAccountCredentials
from configparser import ConfigParser


config_parser = ConfigParser()
config_parser.read('config.ini')

def create_client():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    return gspread.authorize(creds)


<<<<<<< HEAD
#Writing results to the spreadsheet. Column A is date, B is for kcal consumed and C is for kcal burned.
def write_kcal_to_sheet(client, nutri_kcal, endo_kcal, date):
    sheet_name = config_parser.get('Google API', 'sheetname')
    sheet = client.open(sheet_name).sheet1
=======
def write_data_to_sheet(client, nutri_kcal, endo_kcal, weight, fat, water, bone, muscle, date):

    sheet = client.open("Nutridata_Endomondo").sheet1
>>>>>>> garmin
    cell_list = sheet.findall(date)

    date_cell_row = cell_list[0].row
    sheet.update_acell('B' + str(date_cell_row), nutri_kcal)
    sheet.update_acell('C' + str(date_cell_row), endo_kcal)
    sheet.update_acell('D' + str(date_cell_row), weight)
    sheet.update_acell('E' + str(date_cell_row), fat)
    sheet.update_acell('F' + str(date_cell_row), water)
    sheet.update_acell('G' + str(date_cell_row), bone)
    sheet.update_acell('H' + str(date_cell_row), muscle)
