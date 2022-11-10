import glob

months = {
  '1':'Jan',
  '2':'Feb',
  '3':'Mar',
  '4':'Apr',
  '5':'May',
  '6':'Jun',
  '7':'Jul',
  '8':'Aug',
  '9':'Sep',
  '10':'Oct',
  '11':'Nov',
  '12':'Dec'
  }

def get_files_by_year(location,year):
  filenames = []
  for month in months:
   filenames.append(glob.glob( location + "/*" + year + "_" + months[month] + ".txt" ))
  return list(filter(None, filenames))

def get_file_by_month(location,year,month):
  filename = glob.glob(location + "/*" + year + "_" + months[month] + ".txt" )
  return filename
