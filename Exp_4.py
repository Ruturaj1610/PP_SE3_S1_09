# -*- coding: utf-8 -*-
"""PP_EXP_4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xXPysiOLfna0iZI_qj2Uk_l0p-rZilo0
"""

from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    file = open (filename, method)
    yield file
    file.close ()

if __name__== '__main__':
    try:
      with genericFileFunction("test.txt",'w')as f:
          f.write("Hello , I am Ruturaj")

      with genericFileFunction("test.txt",'r')as f:
          print(f.read())

      with genericFileFunction("test.txt",'a')as f:
          f.write("\nThis line is appneded")

      with genericFileFunction("test.txt",'r')as f:
          print(f.read())

    except Exception as e:
      print(e)

