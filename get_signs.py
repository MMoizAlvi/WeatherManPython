from operator import ge, ne
from termcolor import colored

def gen_sign_red(tempratureValue):
  sign = ''
  for index in range(tempratureValue):
   sign += colored('+', 'red')
  return sign

def gen_sign_blue(tempratureValue):
  sign = ''
  for index in range(tempratureValue):
   sign += colored('+', 'blue')
  return sign
