#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program Name: fix_kr_id3.py
Description:
KoreanID3Fixer is a Python program to fix the Korean encoding issue
for ID3 attributes for MP3 files. This provides an easy-to-use solution
for updating the metadata of songs in a folder.
Author: Michael Han <clayjar@gmail.com>

Last Updated: 2023-08-03
Python Version: 3.10.12
License: MIT
"""

# encoding: utf-8
import glob
import os
import re
from mutagen.easyid3 import EasyID3
# easy_install mutagen

quiet = False

def convert_encoding(input_string):
    source = ['iso-8859-9','iso-8859-1','cp949']
    # target = 'utf-8'
    target = 'euc-kr'

    for encoding in source:
      try:
          final_string = input_string.encode(encoding).decode(target)
          return final_string

      except UnicodeEncodeError:
          print("The string contains characters that are not supported in '%s' encoding." % encoding)
          continue
      except UnicodeDecodeError:
          print("The string could not be decoded using '%s' encoding." % (target))
          continue

    return None

def fix_kr_tag(f, tag):
  try:
    title = f[tag][0]
    converted = convert_encoding(title)

    if title == converted:
      return False
    if not quiet:
      print("  %s = %s" % (tag, converted))
    f[tag]=converted
    return True
  except:
    pass
    return False

def fix_kr_encoding(path):
  needSave = False
  f = EasyID3(path)
  for tag in list(f.keys()):
    if fix_kr_tag(f, tag):
      needSave = True

  if needSave: 
    if not quiet:
      print("updating %s" % path)
    f.save()

def fix_dir(directory):
  directory = re.sub(r'\[', '[[]', directory)
  directory = re.sub(r'(?<!\[)\]', '[]]', directory)

  for path in glob.glob(directory+"/*.[Mm][Pp]3"):
    if not quiet:
      print("checking %s" % path)
    fix_kr_encoding(path)

def main():
  fix_dir(os.getcwd())

if __name__ == "__main__":
  main()

