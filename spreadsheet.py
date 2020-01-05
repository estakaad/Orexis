import gspread
from oauth2client.service_account import ServiceAccountCredentials


def create_client():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    return gspread.authorize(creds)


def write_kcal_to_sheet(client, nutri_kcal, endo_kcal, date):

    sheet = client.open("Nutridata_Endomondo").sheet1
    cell_list = sheet.findall(date)

    date_cell_row = cell_list[0].row
    sheet.update_acell('B' + str(date_cell_row), nutri_kcal)
    sheet.update_acell('C' + str(date_cell_row), endo_kcal)