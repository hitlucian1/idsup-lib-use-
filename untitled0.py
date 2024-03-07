
from matplotlib import pyplot as x
from collections import Counter
'''
years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.2,1075.9,2862.5,5979.6,10289.7,14958.3]
x.plot(years,gdp,color='red',marker='*',linestyle='--')
x.title('year and gdp')
x.xlabel('year')
x.ylabel('gdp')
x.show()
'''
#bar graph
'''
movies=['chaichom','manas the last air bender','omm the mahavir','sibu the designer', 'sambhav the nalua']
num_awards=[5,11,3,8,10]
x.bar(movies,num_awards,color='green', edgecolor='red',width=0.5)
x.yticks(range(21))
'''
#histograph
'''
grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]
lst=[min(i// 10*10,90) for i in grades]
print(lst)
histogram=Counter(lst)
print(histogram)
x.bar([x+10 for x in histogram.keys()],histogram.values(),width=10)
x.xticks([10*i for i in range(11)])
'''
'''variance=[1,2,4,8,16,32,64,128,256]
bias_sq=[256,128,64,32,16,8,4,2,1]
total_error=[x+y for x,y in zip(variance,bias_sq)]
xs=[i for i,_ in enumerate(variance)]
x.plot(xs,variance,'g-',label='variance')
x.plot(xs,bias_sq,'r-',label='bias_sq')
x.plot(xs,total_error,'b-',label='total_error')
x.legend(loc=9)
x.xticks([])'''

#scatterplot
users=[70,65,72,63,71,64,60,64,67]
minutes=[175,170,205,120,220,130,105,145,190]
website=['a','b','c','d','e','f','g','h','i']
x.scatter(users,minutes)
for i,j,k in zip(website,users,minutes):
    x.annotate(i,xy=(j,k),xytext=(10,-10),textcoords='offset points')