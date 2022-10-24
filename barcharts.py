import GetFiles
import pandas
import get_signs


def get_temperature_chart(location, year, month):
  cs = pandas.read_csv(GetFiles.get_file_by_month(location, year, month)[0])

  b = cs[['Max TemperatureC','Min TemperatureC']].dropna()
  for index , row in b.iterrows():
    print(index,get_signs.gen_sign_red(int(row[0])), row[0],'C')
    print(" ",get_signs.gen_sign_blue(int(row[1])), row[1],'C')


def get_advanced_temperature_chart(location, year, month):
  cs = pandas.read_csv(GetFiles.get_file_by_month(location, year, month)[0])
  b = cs[['Max TemperatureC','Min TemperatureC']].dropna()
  for index , row in b.iterrows():
    print(index,get_signs.gen_sign_blue(int(row[1])), get_signs.gen_sign_red(int(row[0])), row[1],'C -',row[0],'C')

