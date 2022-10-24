import GetFiles
import pandas
import Formated_date


def get_max_Avg_temperature(location, year, month):
  cs = pandas.read_csv(GetFiles.get_file_by_month(location, year, month)[0])
  b = int(cs[['Mean TemperatureC']].dropna().idxmax())
  return Formated_date.get_formated_date(cs.iloc[b][0]), cs.iloc[b][2]

def get_min_Avg_temperature(location,year,month):
  cs = pandas.read_csv(GetFiles.get_file_by_month(location, year, month)[0])
  b = int(cs[['Mean TemperatureC']].dropna().idxmin())
  return Formated_date.get_formated_date(cs.iloc[b][0]), cs.iloc[b][2]


def get_Avg_Humidity(location,year,month):
  cs = pandas.read_csv(GetFiles.get_file_by_month(location, year, month)[0])
  mean = list(cs[[' Mean Humidity']].dropna().mean())
  return mean
