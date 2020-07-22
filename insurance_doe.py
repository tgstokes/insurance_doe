#import libs
import numpy as np
import pandas as pd
# define files
file_to_open = r"C:\Users\tgsto\GitHub\insurance_doe\insurance parameters.txt"
sweep_file_to_open = r"C:\Users\tgsto\GitHub\insurance_doe\sweep parameters.txt"
# define functions
def read_param_file(file_to_open):
    file_read = {}
    with open(file_to_open) as fo:
        for line in fo:
            line_to_read = line.strip()
            fields = line_to_read.split(":")
            param = fields[0]
            param_value = fields[1]
            file_read.update({param:param_value})
    return file_read

def read_sweep_file(file_to_open):
    file_read = {}
    with open(file_to_open) as fo:
        for line in fo:
            line_to_read = line.strip()
            fields = line_to_read.split(":")
            param = fields[0]
            param_min = fields[1]
            param_max = fields[2]
            file_read.update({param:[param_min, param_max]})
    return file_read

def check_floats(dic, print_on = 0):
    for key in dic.keys():
        try:
            dic.update({key:float(dic[key])})
        except ValueError:
            if print_on == 1:
                print("skipping: Value ", dic[key], " is not a float...")
    return dic

def check_ints(dic, print_on = 0):
    for key in dic.keys():
        try:
            dic.update({key:int(dic[key])})
        except ValueError:
            if print_on == 1:
                print("skipping: Value ", dic[key], " is not a float...")
    return dic
#define method
file_read = read_param_file(file_to_open)
output_dict = check_ints(file_read)
print(output_dict)
sweep_read = read_sweep_file(sweep_file_to_open)
print(sweep_read)