import GetFiles

def get_formated_date(date):
  date=date.split('-')
  return GetFiles.months[date[1]]+' '+date[2]
