import pandas
import sys
import get_files
import formated_date

def get_max_temperature(location, year):
  temperatures = get_temp_data(location, year, 'Max TemperatureC', 1)
  return sorted(temperatures.items(), key = lambda item: item[1])[-1]

def get_min_temperature(location, year):
 temperatures = get_temp_data(location, year, 'Min TemperatureC', 3)
 return sorted(temperatures.items(), key = lambda item: item[1])[-1]

def get_max_humidity(location, year):
 temperatures = get_temp_data(location, year, 'Max Humidity', 7)
 return sorted(temperatures.items(), key = lambda item: item[1])[-1]

def get_temp_data(location, year, type, index):
  temperatures = {}
  filenames = get_files.get_files_by_year(location, year)
  for file in filenames:
    fileData = pandas.read_csv(file[0])
    fetchedRow = int(fileData[[type]].dropna().idxmax())
    temperatures[formated_date.get_formated_date(fileData.iloc[fetchedRow][0])] = fileData.iloc[fetchedRow][index]
  return temperatures
