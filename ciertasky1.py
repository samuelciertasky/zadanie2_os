#!/usr/bin/env python3

sum = v_sum = 0

def list_eval(item,d):
    v_x = []

    for x in item:
        if isinstance(x,int) or isinstance(x,float):
            v_x.append(x)
        elif isinstance(x,str):
            if x =='+' or x == '-' or x == '*' or x == '/':
                v_symb = x
            else:
                v_x.append(d[x])
        else:
            list_x = list_eval(x,d)
            v_x.append(list_x)

    if v_symb == '+':
        v_sum = v_x[0] + v_x[1]
    elif v_symb == '-':
        v_sum = v_x[0] - v_x[1]
    elif v_symb == '*':
        v_sum = v_x[0] * v_x[1]
    else:
        v_sum = v_x[0] / v_x[1]

    return v_sum

def myevald(f,d={}):
    value = []

    if isinstance(x,int) or isinstance(x,float):
        return f
    elif isinstance(x,str):
        return d[f]
    elif isinstance(f,list):

        for item in f:
            if isinstance(item,int) or isinstance(item,float):
                value.append(item)

            elif isinstance(item,str):
                if x =='+' or x == '-' or x == '*' or x == '/':
                    symb = item
                else:
                    value.append(d[item])
            else:
                list_sum = list_eval(item,d)
                value.append(list_sum)
        if symb == '+':
            sum = value[0] + value[1]
        elif v_symb == '-':
            sum = value[0] - value[1]
        elif v_symb == '*':
            sum = value[0] * value[1]
        else:
            sum = value[0] / value[1]
    return sum

def myderive(f,var={}):
    value = []

    if isinstance(x,int) or isinstance(x,float):
        return 0;
    if isinstance(x,str):
        if x == var:
            return 1
        else:
            return 0
