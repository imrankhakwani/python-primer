import os, shutil, time

home = os.getcwd()

# print(home)

# os.mkdir("new")

# os.rmdir("old")
# os.system('ls -al')

# root_scr_dir = r'./'
# root_dst_dir = r'./backup-' + time.asctime()
#
# for src_dir, dirs, files in os.walk(root_scr_dir):
#     dst_dir = src_dir.replace(root_scr_dir, root_dst_dir, 1)
#     if not os.path.exists(dst_dir):
#         os.makedirs(dst_dir)
#     for file_ in files:
#         src_file = os.path.join(src_dir, file_)
#         dst_file = os.path.join(dst_dir, file_)
#         if os.path.exists(dst_file):
#             os.remove(dst_file)
#         shutil.copy(src_file, dst_dir)
# print(">>>>>>>>>>>>>>>>>>>>Backup Complete<<<<<<<<<<<<<<<<<<")

os.system('ls -al')

# student = {"name": 'Imran Saeed', 'job': 'Web Developer'}
#
# student['abd'] = "New Entry"
#
# print(student.get("abd", "Sorry! key not found."))
#
# print(student.pop('abd'))
#
# print(student.keys())
# print(student.values())
# print(student.items())
#
# for key, value in student.items():
#     print(key + ': ' + value)
#
# if student['job'] == 'IT Pro':
#     print('IT Professional')
# elif student['job'] == 'Web Developer':
#     print('Web Developer')
# else:
#     print('Other then IT')
#
# condition = {}
#
# if condition:
#     print('True')
# else:
#     print('False')

# numbers = [1,2,3,4,5,6,7,8,9,0]
# for number in numbers:
#     for letter in 'abc':
#         print(number, letter)
#
# for num in range(0, 3):
#     print(num)

# a = 0o267
# b = 0xFD23C
# c = 0b1101110001
# f = 1.79e308
#
# print(a)
# print(b)
# print(c)
# print(f)
#
# print(type(2+3j))
#
# print('this is a string enclosed by single quotes and contains a \' character')
#
# # TAB character \t
# print("a\tb")
#
# # letter 'a'
# print("a\141\x61")
#
# # new line character \n
# print("a\nb")
#
# # right arrow ascii character
# # \u2192                unicode
# # \N{rightwards arrow}  verbose
# print('\u2192 \N{rightwards arrow}')
#
# # raw string, ignore escape characters
# # preceded with 'r' or 'R'
# print(r'\u2192 \N{rightwards arrow}')
# print(R'\u2192 \N{rightwards arrow}')
#
# print('''This string has a single (') and a double (") quote.''')
#
# print("""A quick clever
# brown fox
# jumps over the
# lazy dog.""")
#
# print('\n')
#
# print('Truth Table for OR operation:')
# print('True or False: ', True or False)
# print('True or True: ', True or True)
# print('False or True: ', False or True)
# print('False or False: ', False or False)
#
# print('\n')
#
# print('Truth Table for AND operation:')
# print('True and False: ', True and False)
# print('False and True: ', False and True)
# print('False and False:', False and False)
# print('True and True:', True and True)
#
# name = 'imran saeed'
# print(name.split(sep=' '))
# print(name.capitalize())
# print(name.upper())
# print(name.center(30, '-'))
# print(name.index('saeed'))
# print(name.title())


import calendar

sep = calendar.TextCalendar(calendar.MONDAY)
# sep.prmonth(1974, 3)
#
# print(calendar.leapdays(2000, 2023))
#
# print(calendar.prcal(2023))

# for i in sep.itermonthdays(2023, 7):
#     print(i)
#
# for month in calendar.month_name:
#     print(month)
#
# for day in calendar.day_name:
#     print(day)
#
# for day_abr in calendar.day_abbr:
#     print(day_abr)
#
# for mon_abr in calendar.month_abbr:
#     print(mon_abr)
#
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# print(hc.formatmonth(2023, 7))
#
# import math
#
# print(math.sin(2))
#
# from math import floor as f
# print(f(1.9723))
#
# import math as m
# print(m.ceil(1.25))

from math import *
# print(trunc(5.99999))
#
# print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
#
# print(fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

# print(exp(1e-5) - 1)
#
# print(expm1(1e-5))
#
# print(math.e)
# print(math.pi)

import random
import math

# print(random.randint(1, 5))
#
# print(math.trunc(random.random() * 100))
#
# colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
#
# print(random.choice(colors))
#
# random.shuffle(colors)
#
# print(colors)

# lst = [[i] for i in range(20)]
#
# print(lst)
#
# random.shuffle(lst)
#
# print(lst)
#
# print(random.randrange(0, 200, 7))
#
# output = {"Heads": 0, "Tails": 0}
# coin = list(output.keys())
#
# for i in range(10000):
#     output[random.choice(coin)] += 1
#
# print("Heads: ", output["Heads"])
# print("Tails: ", output["Tails"])

import tkinter as tk
from tkinter import *

window_ = Tk()