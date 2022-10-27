import get_files

def get_formated_date(date):
  date = date.split('-')
  return get_files.months[date[1]] + ' ' + date[2]
