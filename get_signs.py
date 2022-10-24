from operator import ge, ne
from termcolor import colored

def gen_sign_red(n):
  sign=''
  for i in range(n):
   sign+= colored('+', 'red')
  return sign



def gen_sign_blue(n):
  sign=''
  for i in range(n):
   sign+= colored('+', 'blue')
  return sign
