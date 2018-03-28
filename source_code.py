#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:12:31 2017

@author: ramya
"""

from operator import itemgetter
import collections
import matplotlib.pyplot as plt
import csv
nasdaq_close = {} #collections.OrderedDict()
microsoft = collections.OrderedDict([(('us-autoshow-tesla-battery-interview-sb-idUSTRE50D0RZ20090114', '1/13/2009'), 7), (('us-ford-loans-idUSTRE55M39120090623', '6/23/2009'), 0), (('us-ford-loans-sb-idUSTRE55M4PV20090623', '6/23/2009'), 2), (('us-tesla-toyota-idUSTRE64J70O20100521', '5/21/2010'), -9), (('us-tesla-ipo-idUSTRE65R2B620100628', '6/28/2010'), 2), (('us-markets-stocks-tesla-idUSTRE65S3ZA20100629', '6/29/2010'), 1), (('us-toyota-tesla-idUSTRE6683RA20100709', '7/9/2010'), -3), (('us-tesla-shares-idUSTRE6BQ2CJ20101227', '12/27/2010'), -1), (('us-tesla-shares-idUSTRE6BQ2L920101227', '12/27/2010'), -1), (('us-usa-tesla-idUSTRE7910B420111002', '10/2/2011'), -2), (('us-tesla-idUSBRE8481FS20120509', '5/9/2012'), -2), (('us-tesla-models-idUSBRE85M01Q20120623', '6/22/2012'), 3), (('us-tesla-spacex-idUSBRE87U0KR20120831', '8/31/2012'), 0), (('us-tesla-draper-idUSBRE88B1KU20120912', '9/12/2012'), 0), (('us-tesla-draper-idUSBRE88B1KU20120913', '9/12/2012'), 0), (('us-tesla-outlook-idUSBRE88O0JN20120925', '9/25/2012'), -14), (('us-tesla-results-idUSBRE8A40K420121105', '11/5/2012'), -8), (('us-tesla-ev-idUSBRE8AC03O20121113', '11/12/2012'), -2), (('us-boeing-tesla-idUSBRE90S03I20130129', '1/29/2013'), -8), (('us-tesla-nyt-idUSBRE91P01H20130226', '2/25/2013'), -5), (('us-tesla-libelclaim-bbc-idUSBRE92416O20130305', '3/5/2013'), -27), (('us-tesla-financing-idUSBRE9310YN20130402', '4/2/2013'), 4), (('us-autos-tesla-musk-idUSBRE93215J20130403', '4/3/2013'), 7), (('us-tesla-ceo-idUSBRE93911B20130410', '4/10/2013'), -4), (('us-tesla-ceo-idUSBRE93O13K20130425', '4/25/2013'), 0), (('us-autos-tesla-service-idUSBRE93P16P20130426', '4/26/2013'), -3), (('us-tradingplan-subpoena-idUSBRE93T06T20130430', '4/30/2013'), -3), (('us-autos-tesla-resale-idUSBRE9420WT20130503', '5/3/2013'), -4), (('us-autos-tesla-idUSBRE94716E20130508', '5/8/2013'), 3), (('us-autos-tesla-idUSBRE94716E20130509', '5/8/2013'), -6), (('us-autos-tesla-test-idUSBRE9480E020130509', '5/9/2013'), 0), (('us-autos-tesla-idUSBRE94900720130510', '5/9/2013'), 6), (('us-tesla-loan-idUSBRE94K03F20130521', '5/20/2013'), 0), (('us-tesla-doe-idUSBRE94L16520130522', '5/22/2013'), -3), (('us-autos-tesla-chrysler-idUSBRE94M11D20130523', '5/23/2013'), -3), (('us-autos-tesla-texas-idUSBRE95403C20130605', '6/4/2013'), -7), (('us-tesla-recall-idUSBRE95I0OZ20130619', '6/19/2013'), -16), (('us-fidelity-apple-idUSBRE96U11B20130731', '7/31/2013'), -4), (('us-teslamotors-results-idUSBRE97618K20130807', '8/7/2013'), -7), (('us-china-autos-tesla-idUSBRE97M0D920130823', '8/23/2013'), 2), (('us-tesla-selfdriving-idUSBRE98H01720130918', '9/17/2013'), -4), (('us-autos-tesla-crash-idUSBRE99200020131003', '10/2/2013'), -10), (('us-autos-tesla-fire-idUSBRE9920SX20131003', '10/3/2013'), -20), (('us-autos-tesla-fire-idUSBRE9920SX20131004', '10/4/2013'), -23), (('us-samsung-sdi-idUSBRE99300A20131004', '10/3/2013'), -1), (('us-gm-cadillac-elr-idUSBRE99A0SN20131011', '10/11/2013'), -5), (('us-autos-tesla-idUSBRE99F0UJ20131016', '10/16/2013'), 0), (('us-autos-tesla-field-idUSBRE99N17220131024', '10/24/2013'), 5), (('us-tesla-germany-idUSBRE99P04320131026', '10/26/2013'), 0), (('us-tesla-battery-panasonic-idUSBRE99T0RT20131030', '10/30/2013'), 0), (('us-autos-daimler-tesla-idUSBRE99U0UU20131031', '10/31/2013'), 0), (('us-markets-stocks-idUSBRE99R0GU20131105', '11/5/2013'), 3), (('us-autos-tesla-fire-idUSBRE9A60U220131107', '11/7/2013'), -22), (('us-autos-tesla-fire-idUSBRE9A618L20131107', '11/7/2013'), -22), (('us-autos-tesla-recall-idUSBRE9AB17G20131112', '11/12/2013'), -9), (('us-autos-tesla-investigation-idUSBRE9AI0VX20131119', '11/19/2013'), -34)])
with open('HistoricalQuotes.csv') as f:
    reader = csv.reader(f)
    row_num = 0
    w=[]
    for row in reader:
        if row_num > 0:
            nasdaq_close[row[0]] = float(row[3]) - float(row[1])#open - close
        row_num = row_num+1
#print nasdaq_close 
list_stock_perf = []
list_sentiments = []
for key,value in microsoft.items():
    #print key
    if nasdaq_close.has_key(key[1]):
        list_stock_perf.append((key[1],nasdaq_close[key[1]]))
        list_sentiments.append((key[1], value))
#print list_stock_perf
#print list_sentiments
x_axis = []
y_axis = []

for i, item in enumerate(list_stock_perf):
    x_axis.append(i)
    y_axis.append(item[1])
#dictList = []
#for i in range(len(microsoft.items())):
##    x_axis.append(microsoft.items()[i][0][1])
##    x_axis.append(i)
##    y_axis.append(microsoft.items()[i][1])
#    print microsoft.items()[i][0][1]
#    print microsoft.items()[i][1]

#for x,y in zip(x_axis,y_axis):
#    print x,y
plt.figure(figsize=(10,10))
plt.xlabel('Trading Day')
plt.ylabel('Stock performance')
plt.title('TSLA Stock performance when the stock was in the news')
plt.plot(x_axis,y_axis)

#del x_axis[:]
#del y_axis[:]

x = []
y = []
for i, item in enumerate(list_sentiments):
    x.append(i)
    y.append(item[1])
#dictList = []
#for i in range(len(microsoft.items())):
##    x_axis.append(microsoft.items()[i][0][1])
##    x_axis.append(i)
##    y_axis.append(microsoft.items()[i][1])
#    print microsoft.items()[i][0][1]
#    print microsoft.items()[i][1]

#for x,y in zip(x_axis,y_axis):
#    printabsolute_import

plt.figure(figsize=(10,10))
plt.xlabel('Trading Day')
plt.ylabel('Stock sentiment')
plt.title('Sentiment about TSLA Stock in the news')
plt.plot(x,y)

count = 0
for a,b in zip(y_axis, y):
    if(count < 32):
        print a
        count = count + 1              