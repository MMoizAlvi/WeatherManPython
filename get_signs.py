from termcolor import colored

def generate_sign_red(tempratureValue):
  sign = ''
  for index in range(tempratureValue):
   sign += colored('+', 'red')
  return sign

def generate_sign_blue(tempratureValue):
  sign = ''
  for index in range(tempratureValue):
   sign += colored('+', 'blue')
  return sign
