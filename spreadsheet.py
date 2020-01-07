import gspread
from oauth2client.service_account import ServiceAccountCredentials


def create_client():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    return gspread.authorize(creds)


def write_data_to_sheet(client, nutri_kcal, endo_kcal, weight, fat, water, bone, muscle, date):

    sheet = client.open("Nutridata_Endomondo").sheet1
    cell_list = sheet.findall(date)

    date_cell_row = cell_list[0].row
    sheet.update_acell('B' + str(date_cell_row), nutri_kcal)
    sheet.update_acell('C' + str(date_cell_row), endo_kcal)
    sheet.update_acell('D' + str(date_cell_row), weight)
    sheet.update_acell('E' + str(date_cell_row), fat)
    sheet.update_acell('F' + str(date_cell_row), water)
    sheet.update_acell('G' + str(date_cell_row), bone)
    sheet.update_acell('H' + str(date_cell_row), muscle)
