"""
this calculator contains many different formulas.
in order, these are the things the calculator can calculate:
1 and 2 prop z intervals and tests
1 and 2 sample t tests and intervals
"""

#first to import all the correct programs:
import math
import pandas
from scipy.stats import norm
from scipy.stats import t

#this will be the z tests and intervals calculators

#this is for p-value in all calculators:
def finding_p(sign, conversion):
   if sign == "!=":
       p_value = round(2*(1 - conversion), 3)
   if sign == ">":
       p_value = 1-conversion
   #then it must be "<"
   else:   
       p_value = round(conversion, 3)
   return p_value

#1 proportion standard deviation
def one_prop_sd(x, n):
   pr = x/n
   variance = ((pr * (1-pr))/n)
   standard_dev = variance ** 0.5
   return standard_dev

#this will give us interval or test based on what we ask
def one_proportion(x, n, t, num, sign):
   sd = round(one_prop_sd(x, n), 3)
   p_a = round(x/n, 3)
   if t == "t":
       p_n = float(input("What is your null hypothesis proportion?  "))
       z_value = round((p_a - p_n)/sd,3)
       conversion = norm.cdf(z_value)
       p_value = finding_p(sign, conversion)
       print(
           'Standard Deviation: {0}\nProportion: {1} \nZ-Value: {2}\np_value: {3}'
           .format(sd, p_a, z_value, p_value)
       )
       return p_value
   #in that case it would be "i"
   else:
       z_value =round(norm.ppf(num+ ((1-num)/2)),3)
       m_o_e = round(z_value * sd, 3)
       low = round(p_a - m_o_e, 3)
       high = round(p_a + m_o_e, 3)
       interval = (low, high)
       print(
           'Interval: {0}\nMargin of Error:  {1}\nProportion: {2}\nStandard Deviation: {3}\nz_value: {4}'
           .format(interval, m_o_e, p_a, sd, z_value)
       )

#now we will create the calculator for 2 proportion test and interval
def two_prop_sd(pa, pb, na, nb):
   var_a = (pa * (1-pa))/na
   var_b = (pb * (1-pb))/nb
   sd = (var_a + var_b) ** 0.5
   return sd

def two_prop_z(xa, xb, na, nb, t, num, sign):
   prop_a = round(xa/na, 3)
   prop_b = round(xb/nb, 3)
   diff = prop_a-prop_b
   if t == "t":
       p_h = round(((xa+xb)/(na+nb)), 3)
       stand_dev = round(two_prop_sd(p_h, p_h, na, nb), 3)
       z_value = round(diff/stand_dev, 3)
       conversion = norm.cdf(z_value)
       p_value = finding_p(sign, conversion)
       print(
           'Standard Deviation: {0}\nProportion A: {1}\nProportion B: {2}\np-hat: {3}\nZ-Value: {4}\np_value: {5}'
           .format(stand_dev, prop_a, prop_b, p_h, z_value, p_value)
       )
       return p_value
   #then it is "i"
   else:
       z_value =round(norm.ppf(num+ ((1-num)/2)),3)
       stand_dev = round(two_prop_sd(prop_a, prop_b, na, nb), 3)
       m_o_e = round(z_value * stand_dev, 3)
       low = round(diff - m_o_e, 3)
       high = round(diff + m_o_e, 3)
       interval = (low, high)
       print(
           'Interval: {0}\nMargin of Error:  {1}\nProportion A: {2}\nProportion B: {3}\nStandard Deviation: {4}\nz_value: {5}'
           .format(interval, m_o_e, prop_a, prop_b,  stand_dev, z_value)
       )

#this is for the 1 sample t test and interval
def one_sample_t(x, s, n, t, num, sign):
   standard_deviation = round((s/(n**0.5)), 3)
   if t == "t":
       x_n = float(input("What is your null hypothesis proportion?  "))
       t_value = round((x - x_n)/standard_deviation,3)
       conversion = t.cdf(t_value, n-1)
       p_value = finding_p(sign, conversion)
       print(
           'P-value: {0}\nMean: {1}\nStandard Deviation: {2}\nT-value: {3}'
           .format(p_value, x, s, t_value)
       )
       return p_value
   #the interval otherwise:
   else:
       t_value = round(t.ppf(num + (1-num)/2, n-1), 3)
       m_o_e = round(t * standard_deviation, 3)
       high = round(x + m_o_e, 3)
       low = round(x - m_o_e, 3)
       interval = (low, high)
       print(
           'Interval: {0}\nMargin of Error:  {1}\nMean: {2}\nStandard Deviation(calc): {3}\nt_value: {4}'
           .format(interval, m_o_e, s, standard_deviation, t_value)
       )

def degrees(var_a, var_b, na, nb):
   numerator = (var_a + var_b) ** 2
   multi_a = 1/(na-1)
   multi_b = 1/(nb-1)
   denominator = (multi_a * (var_a ** 2)) + (multi_b * (var_b ** 2))
   return numerator/denominator

def two_sample_t(xa, xb, sa, sb, na, nb, t, num, sign):
   var_a = (sa ** 2)/na
   var_b = (sb ** 2)/nb
   df = round(degrees(var_a, var_b, na, nb), 3)
   standard_dev = round((var_a + var_b) ** 0.5, 3)
   diff = xa - xb
   if t == "t":
       t_value = diff/ standard_dev
       conversion = t.cdf(t_value, df)
       p_value = finding_p(conversion, sign)
       print (
           'P-value: {0}\nx1: {1}\nx2: {2}\ns1: {3}\ns2: {4}\nn1: {5}\nn2: {6}\ndf: {7}\nt_value: {8}'
           .format(p_value, xa, xb, sa, sb, na, nb, df, t_value)
       )
       return p_value
   #now for the interval
   else:
       t_value = round(t.ppf(num + (1-num)/2, df), 3)
       m_o_e = round(t * standard_dev, 3)
       high = round(diff + m_o_e, 3)
       low = round(diff - m_o_e, 3)
       interval = (low, high)
       print (
           'Interval: {0}\nx1: {1}\nx2: {2}\ns1: {3}\ns2: {4}\nn1: {5}\nn2: {6}\ndf: {7}\nMargin of Error: {8}\nt_value: {9}'
           .format(interval, xa, xb, sa, sb, na, nb, df, m_o_e, t_value)
       )

def ask_parameters(parameters):
   print("In order, enter: {}; separated by spaces ".format(parameters))
   answer = input()
   seperators = ", : ; "
   param = "".join(char if char not in seperators else " " for char in answer).split()
   param = ([int(val) for val in param])
   return param


def interval_and_test_calculator():
   print("Are you doing a test or interval(t/i)? Enter qq to quit.")
   t = input()
   print("Are you using proportions or means (z/t)?")
   t_type = input()
   print("1 sample or 2?")
   t_amt = int(input())
   if t == "t":
       print("what is the sign of Ha (<, >, !=)?")
       sign = input()
       print("enter significance level alpha")
       num = float(input())
       print("----------------------------------------------------")
       if t_amt == 1:
           if t_type == "z":
               param = ask_parameters("x, n")
               p_value = one_proportion(param[0], param[1], "t", num, sign)
           if t_type == "t":
               param = ask_parameters("mean, standard deviation, n")
               one_sample_t(param[0], param[1], param[2], "t", num, sign)
       if t_amt == 2:
           if t_type =="z":
               param = ask_parameters("xa, xb, na, nb")
               p_value = two_prop_z(param[0], param[1], param[2], param[3], "t", num, sign)
           if t_type == "t":
               param = ask_parameters("mean1, mean2, sd1, sd2, n1, n2")
               two_sample_t(param[0], param[1], param[2], param[3], param[4], param[5], "t", num, sign)
       print("Reject null hypothesis?: {}".format(num <= p_value))
   if t == "i":
       print("what is the confidence level?")
       num = float(input())
       print("----------------------------------------------------")
       if t_amt == 1:
           if t_type == "z":
               param = ask_parameters("x, n")
               one_proportion(param[0], param[1], "i", num, "=")
           if t_type == "t":
               param = ask_parameters("mean, standard deviation, n")
               one_sample_t(param[0], param[1], param[2], "i", num, "=")
       if t_amt == 2:
           if t_type =="z":
               param = ask_parameters("xa, xb, na, nb")
               two_prop_z(param[0], param[1], param[2], param[3], "i", num, "=")
           if t_type == "t":
               param = ask_parameters("mean1, mean2, sd1, sd2, n1, n2")
               two_sample_t(param[0], param[1], param[2], param[3], param[4], param[5], "i", num, "=")

interval_and_test_calculator()
