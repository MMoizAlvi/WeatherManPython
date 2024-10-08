import yearly
import monthly
import barcharts
import sys

if sys.argv[1] == 'e':
  try:
    maxTemprature = yearly.get_max_temperature(sys.argv[2], sys.argv[3])
    minTemprature = yearly.get_min_temperature(sys.argv[2], sys.argv[3])
    humidity = yearly.get_max_humidity(sys.argv[2], sys.argv[3])
    print('HIGHEST TEMPERATURE : ', maxTemprature[-1], 'C on',maxTemprature[0])
    print('LOWEST TEMPERATURE : ', minTemprature[-1], 'C on',minTemprature[0])
    print('HIGHEST HUMIDITY : ', humidity[-1], '% on',humidity[0])
  except:
   print('PLEASE ENTER A VALID INPUT !!!!')
elif sys.argv[1] == 'a':
  try:
    maxTemprature = monthly.get_max_avg_temperature(sys.argv[2], sys.argv[3], sys.argv[4])
    minTemprature = monthly.get_min_avg_temperature(sys.argv[2], sys.argv[3], sys.argv[4])
    humidity = monthly.get_avg_humidity(sys.argv[2], sys.argv[3], sys.argv[4])
    print('HIGHEST AVERAGE TEMPERATURE : ', maxTemprature[-1], 'C on', maxTemprature[0])
    print('LOWEST AVERAGE TEMPERATURE : ', minTemprature[-1], 'C on', minTemprature[0])
    print('HIGHEST AVERAGE HUMIDITY : ', humidity[-1], '%')
  except:
      print('PLEASE ENTER A VALID INPUT !!!!')
elif sys.argv[1] == 'c':
  try:
    barchart = barcharts.get_temperature_chart(sys.argv[2], sys.argv[3], sys.argv[4])
    advancedBarchart = barcharts.get_advanced_temperature_chart(sys.argv[2], sys.argv[3], sys.argv[4])
    print(barchart)
    print(advancedBarchart)
  except:
     print('PLEASE ENTER A VALID INPUT !!!!')
else:
  print('PLEASE ENTER A VALID INPUT !!!!')
