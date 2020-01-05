import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Nutridata_Endomondo").sheet1

cell_list = sheet.findall('2019-12-20')

date_cell_row = cell_list[0].row
sheet.update_acell('B' + str(date_cell_row), '1800')
sheet.update_acell('C' + str(date_cell_row), '200')