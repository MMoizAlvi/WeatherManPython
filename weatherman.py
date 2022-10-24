import yearly
import monthly
import barcharts
import sys


if sys.argv[1] == 'e':
  try:
    max_temp = yearly.get_max_temperature(sys.argv[2],sys.argv[3])
    min_temp = yearly.get_min_temperature(sys.argv[2],sys.argv[3])
    humidity = yearly.get_max_humidity(sys.argv[2],sys.argv[3])
    print('HIGHEST TEMPERATURE : ',max_temp[-1],'C on',max_temp[0])
    print('LOWEST TEMPERATURE : ',min_temp[-1],'C on',min_temp[0])
    print('HIGHEST HUMIDITY : ',humidity[-1],'% on',humidity[0])
  except:
   print('PLEASE ENTER A VALID INPUT !!!!')
elif sys.argv[1] == 'a':
  try:
    max_temp = monthly.get_max_Avg_temperature(sys.argv[2],sys.argv[3],sys.argv[4])
    min_temp = monthly.get_min_Avg_temperature(sys.argv[2],sys.argv[3],sys.argv[4])
    humidity = monthly.get_Avg_Humidity(sys.argv[2],sys.argv[3],sys.argv[4])
    print('HIGHEST AVERAGE TEMPERATURE : ',max_temp[-1],'C on',max_temp[0])
    print('LOWEST AVERAGE TEMPERATURE : ',min_temp[-1],'C on',min_temp[0])
    print('HIGHEST AVERAGE HUMIDITY : ',humidity[-1],'%')
  except:
      print('PLEASE ENTER A VALID INPUT !!!!')
elif sys.argv[1] == 'c':
  try:
    barchart = barcharts.get_temperature_chart(sys.argv[2],sys.argv[3],sys.argv[4])
    advanced_barchart = barcharts.get_advanced_temperature_chart(sys.argv[2],sys.argv[3],sys.argv[4])
    print(barchart)
    print(advanced_barchart)
  except:
     print('PLEASE ENTER A VALID INPUT !!!!')
else:
  print('PLEASE ENTER A VALID INPUT !!!!')

