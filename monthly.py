import get_files
import pandas
import formated_date

def get_max_avg_temperature(location, year, month):
  fileData = pandas.read_csv(get_files.get_file_by_month(location, year, month)[0])
  fetchedRow = int(fileData[['Mean TemperatureC']].dropna().idxmax())
  return formated_date.get_formated_date(fileData.iloc[fetchedRow][0]), fileData.iloc[fetchedRow][2]

def get_min_avg_temperature(location, year, month):
  fileData = pandas.read_csv(get_files.get_file_by_month(location, year, month)[0])
  fetchedRow = int(fileData[['Mean TemperatureC']].dropna().idxmin())
  return formated_date.get_formated_date(fileData.iloc[fetchedRow][0]), fileData.iloc[fetchedRow][2]

def get_avg_humidity(location, year, month):
  fileData = pandas.read_csv(get_files.get_file_by_month(location, year, month)[0])
  mean = list(fileData[[' Mean Humidity']].dropna().mean())
  return mean
