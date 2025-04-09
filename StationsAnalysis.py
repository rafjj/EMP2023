from random import randint
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import scipy
import csv

# 2001: 110631,81
# 2002: 112492,27
# 2003: 114398,39
# 2004: 118022,16
# 2005: 116479,85
# 2006: 117768,2
# 2007: 119341,52
# 2008: 117624,86
# 2009: 121666,46
# 2010: 123288,8
# 2011: 121900,05
# 2012: 120049,72
# 2013: 113798,96
# 2014: 112510,92
# 2015: 114983,47
# 2016: 116324,53
# 2017: 115071,96
# 2018: 110519,72
# 2019: 111632,07
# 2020: 115724,01
# 2021: 114288,09

ettari = [31410.29,
32237.92,
32334.54,
32901.78,
32564.95,
32665.3,
33746.49,
33082.28,
34923.86,
35816.14,
35536.03,
34515.08,
32564.48,
32386.39,
33001.4,
33614.06,
33050.73,
31664.77,
32104.14,
33136.24,
32967.12]

def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")

def conv(ti):
    to = []
    for t in ti: 
        to.append(t-273.15)
    return to

avgs = []

with open('tmaxavg.txt') as f:
    for line in f:
        #print(line)
        a = float(line)
        avgs.append(a)

yearAvgs = []
avg = 0
i = 0
while(i<len(avgs)):
    sub = avgs[i:i+12]
    avg = 0
    for value in sub: 
        avg += value
    avg = avg / 12
    yearAvgs.append(avg)
    i += 13

avgs = conv(avgs)
yearAvgs = conv(yearAvgs)

ma = avgs[:len(avgs)-1]
ya = yearAvgs[:len(yearAvgs)-1]
    
plt.plot(ma)
plt.ylabel('TMAX by month')
plt.show()

x = np.linspace(1957, 2022, 59)
plt.plot(x, ya, 'ro')
plt.ylabel('TMAX by year')
plt.show()

ics = []
for x in yearAvgs: 
    ics.append(randint(0,10))
ics.sort()
icsa = ics[:len(yearAvgs)-1]
plt.plot(icsa, ya, 'ro')
plt.show()
r, p = scipy.stats.pearsonr(icsa, ya)
coef = np.polyfit(icsa,ya,1)
poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(icsa, ya, 'ro', icsa, poly1d_fn(icsa), '--k') #'--k'=black dashed line, 'yo' = yellow circle marker
plt.show()

ssYears = []
ssYears2 = []
with open('SAN SEBASTIANO PO_giornalieri_2007_2021.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    ssSum = 0
    ssSum2 = 0
    sY = 2007
    counter = 0
    flag = False
    for row in csv_reader:
        if flag:
            cY = int(row[0].split("/")[2])
            #print(row)
            if cY != sY:
                ssYears.append(ssSum/counter)
                ssYears2.append(ssSum2/counter)
                counter = 0
                ssSum = 0
                ssSum2 = 0
                sY = cY
            try:
                ssSum += float(Replace(row[1]))
                ssSum2 += float(Replace(row[2]))
            except ValueError:
                counter -= 1
            counter += 1
        else:
            print(row)
        flag = True

for value in ssYears:
    print(value)

for value in ssYears2:
    print(value)

x = np.linspace(2007, 2021, 14)
plt.plot(x, ssYears, 'ro')
plt.ylabel('Portata fiume (mc/s) per anno')
plt.show()

plt.plot(x, ssYears2, 'ro')
plt.ylabel('Livello idrometrico fiume (m) per anno')
plt.show()

tYears = []
tYears2 = []
with open('TAVAGNASCO DORA BALTEA_giornalieri_2002_2021.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    tSum = 0
    tSum2 = 0
    sY = 2002
    counter = 0
    flag = False
    for row in csv_reader:
        if flag:
            cY = int(row[0].split("/")[2])
            #print(row)
            if cY != sY:
                tYears.append(tSum/counter)
                tYears2.append(tSum2/counter)
                counter = 0
                tSum = 0
                tSum2 = 0
                sY = cY
            try:
                tSum += float(Replace(row[1]))
                tSum2 += float(Replace(row[2]))
            except ValueError:
                counter -= 1
            counter += 1
        else:
            print(row)
        flag = True

for value in tYears:
    print(value)

for value in tYears2:
    print(value)

#x = np.linspace(2002, 2021, 19)
#ax = plt.figure().gca()
#ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.plot(ettari[2:], tYears, 'ro')
plt.ylabel('Portata fiume (mc/s) per anno ')
plt.show()

r, p = scipy.stats.pearsonr(ettari[2:], tYears)
coef = np.polyfit(ettari[2:],tYears,1)
poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(ettari[2:], tYears, 'ro', ettari[2:], poly1d_fn(ettari[2:]), '--k') #'--k'=black dashed line, 'yo' = yellow circle marker
plt.show()

print("R:"+str(r))
print("\np:"+str(p))
#plt.plot(x, tYears2)
#plt.ylabel('Livello idrometrico fiume (m) per anno')
#plt.show()
r, p = scipy.stats.pearsonr(ettari[2:], tYears2)
print("R:"+str(r))
print("\np:"+str(p))
coef = np.polyfit(ettari[2:],tYears2,1)
poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(ettari[2:], tYears2, 'ro', ettari[2:], poly1d_fn(ettari[2:]), '--k') #'--k'=black dashed line, 'yo' = yellow circle marker
plt.show()



#San Sebastiano 

num = 7



r, p = scipy.stats.pearsonr(ettari[num:], ssYears)
print("R:"+str(r))
print("\np:"+str(p))
coef = np.polyfit(ettari[num:],ssYears,1)
poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(ettari[num:], ssYears, 'ro', ettari[num:], poly1d_fn(ettari[num:]), '--k') #'--k'=black dashed line, 'yo' = yellow circle marker
plt.show()

r, p = scipy.stats.pearsonr(ettari[num:], ssYears2)
print("R:"+str(r))
print("\np:"+str(p))
coef = np.polyfit(ettari[num:],ssYears2,1)
poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(ettari[num:], ssYears2, 'ro', ettari[num:], poly1d_fn(ettari[num:]), '--k') #'--k'=black dashed line, 'yo' = yellow circle marker
plt.show()

x = np.linspace(2001, 2021, 21)
ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))


plt.plot(x, ettari)
plt.ylabel("Ettari in piemonte")
plt.show()
