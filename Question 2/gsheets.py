from gsheets import Sheets
sheets = Sheets.from_files('credentials.json')
sheets

#https://docs.google.com/spreadsheets/d/1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc/edit?usp=sharing
#sheets['1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc']

url='https://docs.google.com/spreadsheets/d/1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc/edit?usp=sharing'
s=sheets.get(url)
#s.find('Tabellenblatt2')
s.sheets[0].to_csv('Spam.csv', encoding='utf-8', dialect='excel')
csv_name = lambda infos: '%(title)s - %(sheet)s.csv'
s.to_csv(make_filename=csv_name)

