import pandas
import sys
import GetFiles
import Formated_date


def get_max_temperature(location, year):
 temperatures = {}
 filenames = GetFiles.get_files_by_Year(location, year)
 for file in filenames:
  cs = pandas.read_csv(file[0])
  b=int(cs[['Max TemperatureC']].dropna().idxmax())
  temperatures[Formated_date.get_formated_date(cs.iloc[b][0])] = cs.iloc[b][1]
 return sorted(temperatures.items(), key=lambda item: item[1])[-1]


def get_min_temperature(location, year):
 temperatures = {}
 filenames = GetFiles.get_files_by_Year(location, year)
 for file in filenames:
  cs = pandas.read_csv(file[0])
  b=int(cs[['Min TemperatureC']].dropna().idxmin())
  temperatures[Formated_date.get_formated_date(cs.iloc[b][0])] = cs.iloc[b][3]
 return sorted(temperatures.items(), key=lambda item: item[1])[-1]


def get_max_humidity(location, year):
 temperatures = {}
 filenames = GetFiles.get_files_by_Year(location, year)
 for file in filenames:
  cs = pandas.read_csv(file[0])
  b=int(cs[['Max Humidity']].dropna().idxmax())
  temperatures[Formated_date.get_formated_date(cs.iloc[b][0])] = cs.iloc[b][7]
 return sorted(temperatures.items(), key=lambda item: item[1])[-1]



