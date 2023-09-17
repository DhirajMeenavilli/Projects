import random as rand
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10, 10]
import statistics
import itertools

yearly_returns = pd.read_csv('Yearly_returns.txt', sep='\t')
yearly_returns = yearly_returns.sort_values(by=['Year']) #I did it from 2022 to 1922 accidently so I'm flipping the returns
yearly_returns = yearly_returns.reset_index(drop=True)

level= []
year = []
# 100
# yearly_returns.iloc[0]['Year']
# year[0] = int(year[0])
for i in range(120):
    
    level.append([100])
    year.append([int(yearly_returns.iloc[i]['Year'])])

    for j in range(30):
        level[i].append(level[i][j]*(1+(yearly_returns['Return'][i+j+1]/100)))
        year[i].append(year[i][j]+1)
        
for i in range(len(level)):
    plt.title("S&P 500 Normalised Price Chart")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.plot(year[i], level[i], color ="green")
    plt.show()
#     plt.clear()

returns = []
for j in range(len(level)):
    returns.append([])
    for i in range(len(level[j])):
        CAGR_return = round(((level[j][len(level[j])-1]/level[j][i])**(1/(len(level[j])-i))-1),4)
        returns[j].append(CAGR_return)

    # returns = returns[70:len(returns)-40]
    # year = year[70:len(year)-40]

    plt.title("S&P 500 Returns Chart")
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.plot(year[j], returns[j], color ="green")
    plt.show()
    print(returns[j])
    print(year[j])

for j in range(len(returns)):
    geometric = 1
    for i in range(len(returns[j])):
        geometric = geometric * (1+returns[j][i])

    print(year[j][0],"The geometric mean is ~"+str(round((10**(math.log(geometric,10)/len(returns[j]))-1)*100,1))+"%")

passiveInvestor = []

marketTimer = []

treasuryTimer = []
treasuryYield = 1.05

years = []

putTimer = []
putCosts = 0
contractsPurchased = 0

passivePutTimer = []
passiveContractsPurchaed = 0

for j in range(len(returns)):
    passiveInvestor.append([])
    
    passivePutTimer.append([])
    
    marketTimer.append([])
    lastAddition = 0
    
    treasuryTimer.append([])
    bondAllocation = []
    
    putTimer.append([])
    putTimerCash = []
    lastAdditionPut = 0
    
    years.append(year[j][0])
    
    for i in range(len(returns[j])):
        ###---Passive Investor TFSA---###
        passiveInvestor[j].append(6000)
        for k in range(len(passiveInvestor[j])):
            passiveInvestor[j][k] = passiveInvestor[j][k]*(1+returns[j][k])
        
        ###---Passive Put Timer---###
        
        if int(((level[j][i]/level[j][i-1])-1)*100) <= -20 and i > 0: #Might be double counting by doing append so maybe should check if there's sumin already there then add otherwise append
            passivePutTimer[j].append((level[j][i-1]*0.8 - level[j][i]) * 100 * contractsPurchased)
        
        passiveContractsPurchased = 0   
        
        if returns[j][k] > 0.06:
            passivePutTimer[j].append(6000)
        else:
            passiveContractsPurchased = 4000/(level[j][i])
            passivePutTimer[j].append(2000)
        
        for k in range(len(passiveInvestor[j])):
            passivePutTimer[j][k] = passivePutTimer[j][k]*(1+returns[j][k])
        
        ###---Market Timer TFSA w/ options between the market and cash and omniscience---###
        if returns[j][i] >= 0.1:
            marketTimer[j].append(6000*(i+1-lastAddition))
            #print(6000*(i+1-lastAddition),i+1)
            lastAddition = i+1

        else:
            if i == len(returns[j]) - 1:
                marketTimer[j].append(6000*(i+1-lastAddition))

            else:
                marketTimer[j].append(0)

        for k in range(len(marketTimer[j])):
            marketTimer[j][k] = marketTimer[j][k] * (1+returns[j][k])
        
        ###---Market Timer TFSA w/ options between the market and short term treasuries and omniscience---###
        if returns[j][i] >= 0.1: #Change the metric from 0.1 to something more reasonable like Tobins Q.
            if i > 0 and len(bondAllocation) != 0:
                treasuryTimer[j].append(sum(bondAllocation))
                bondAllocation = bondAllocation*0
                
            else:
                treasuryTimer[j].append(6000)
        
        else:
            if i == len(returns[j]) - 1:
                treasuryTimer[j].append(sum(bondAllocation))
                bondAllocation = bondAllocation*0

            else:
                treasuryTimer[j].append(0)
                bondAllocation.append(6000)

        for k in range(len(treasuryTimer[j])):
            treasuryTimer[j][k] = treasuryTimer[j][k] * (1+returns[j][k])
        
        for k in range(len(bondAllocation)):
            bondAllocation[k] = bondAllocation[k]*treasuryYield
            
        ###---Market Timer TFSA w/ options between the market and short term treasuries w/o omniscience---###
#         if returns[j][i] >= 0.10: #Change the metric from 0.1 returns to something more reasonable like Tobins Q.
#             if i > 0:
#                 treasuryTimer[j].append(sum(bondAllocation))
#                 print(bondAllocation)
#                 bondAllocation = bondAllocation*0
#                 print(bondAllocation)
#             else:
#                 treasuryTimer[j].append(6000)
#         else:
#             if i == len(returns[j]) - 1:
#                 treasuryTimer[j].append(sum(bondAllocation))

#             else:
#                 treasuryTimer[j].append(0)
#                 bondAllocation.append(6000)

#         for k in range(len(treasuryTimer[j])):
#             treasuryTimer[j][k] = treasuryTimer[j][k] * (1+returns[j][k])
#             bondAllocation[k] = bondAllocation[k]*treasuryYield
        
        ###---Market Timer with Puts TFSA---###
        if int(((level[j][i]/level[j][i-1])-1)*100) <= -20 and i > 0:#Make the putCost and putProfit more "realistic"
    #         print(i)
#             putProfit = (int(((level[j][i]/level[j][i-1])-1)*-100)/30)*(sum(putTimer[j]) + sum(putTimerCash))* 0.1
            putProfit = (level[j][i-1]*0.8 - level[j][i]) * 100 * contractsPurchased
            putTimerCash.append(putProfit)
            putProfit = 0
            putCosts = 0
        
        contracts_purchased = 0
        
        if sum(putTimerCash) < 0:
            putTimerCash = putTimerCash*0
            
        if returns[j][i] >= 0.1:
            if len(putTimerCash) != 0:
                putTimer[j].append(sum(putTimerCash))
                putTimerCash = []
                putCosts = 0

            else:
                putTimer[j].append(6000)
            
            lastAdditionPut = i+1

        else:
            if i == len(returns[j]) - 1:
                putTimer[j].append(sum(putTimerCash))

            else:
                putTimer[j].append(0)
                putTimerCash.append(6000)
                putCosts = (sum(putTimer[j]) + sum(putTimerCash))* 0.05
                contractsPurchased = math.ceil((putCosts)/(level[j][i]))#Gonna have to write out a Blck Scholes function but that's fine but later.
                putTimerCash.append(putCosts*-1)

        for k in range(len(putTimer[j])):
            putTimer[j][k] = putTimer[j][k] * (1+returns[j][k])

#     passiveTotal = "{:,}".format(round(sum(passiveInvestor[j])))
#     timerTotal = "{:,}".format(round(sum(marketTimer[j])))
#     putTotal = "{:,}".format(round(sum(putTimer)))

#     print(year[j][0],"The Passive Investor gets:",passiveTotal,"The Market Timer gets:",timerTotal)#,"The Put Timer gets:", putTotal)

#     biggestContributorPassive = passiveInvestor[j].index(max(passiveInvestor[j]))
#     biggestContributorTimer = marketTimer[j].index(max(marketTimer[j]))
#     biggestContributorPut = putTimer.index(max(putTimer))

#     print(passiveInvestor)
#     print(marketTimer)

passive = []
passivePutter = []
timer = []
treasury = []
put = []

for i in range(0,len(passiveInvestor)):
    passive.append(round(sum(passiveInvestor[i])))
    passivePutter.append(round(sum(passivePutTimer[i])))
    timer.append(round(sum(marketTimer[i])))
    treasury.append(round(sum(treasuryTimer[i])))
    put.append(round(sum(putTimer[i])))

# years = years[30:]   
    
print("Passive Investor 100 Paths Max:{:,},".format(max(passive)), "Min:{:,},".format(min(passive)), "Median:{:,},".format(round(statistics.median(passive))), "25th:{:,},".format(round(np.percentile(passive, 25))),"75th:{:,}".format(round(np.percentile(passive, 75))),"5th:{:,}".format(round(np.percentile(passive, 5))))
print()
print("Passive Put Timer 100 Paths Max:{:,},".format(max(passivePutter)), "Min:{:,},".format(min(passivePutter)), "Median:{:,},".format(round(statistics.median(passivePutter))), "25th:{:,},".format(round(np.percentile(passivePutter, 25))),"75th:{:,}".format(round(np.percentile(passivePutter, 75))),"5th:{:,}".format(round(np.percentile(passivePutter, 5))))
print()
print("Market Timer Cash 100 Paths Max:{:,},".format(max(timer)), "Min:{:,},".format(min(timer)), "Median:{:,},".format(round(statistics.median(timer))), "25th:{:,},".format(round(np.percentile(timer, 25))),"75th:{:,}".format(round(np.percentile(timer, 75))),"5th:{:,}".format(round(np.percentile(timer, 5))))
print()
print("Market Timer Treasuries 100 Paths Max:{:,},".format(max(treasury)), "Min:{:,},".format(min(treasury)), "Median:{:,},".format(round(statistics.median(treasury))), "25th:{:,},".format(round(np.percentile(treasury, 25))),"75th:{:,}".format(round(np.percentile(treasury, 75))),"5th:{:,}".format(round(np.percentile(treasury, 5))))
print()
print("Market Timer Puts 100 Paths Max:{:,},".format(max(put)), "Min:{:,},".format(min(put)), "Median:{:,},".format(round(statistics.median(put))), "25th:{:,},".format(round(np.percentile(put, 25))),"75th:{:,}".format(round(np.percentile(put, 75))),"5th:{:,}".format(round(np.percentile(put, 5))))
    

plt.title("S&P 500 Returns Chart")
plt.xlabel("Time")
plt.ylabel("Returns")

plt.plot(years, passive, color ="green", label = "Passive")
plt.plot(years, passivePutter, color ="yellow", label = "Passive Putter")
plt.plot(years, timer, color ="orange", label = "Timer")
plt.plot(years, treasury, color ="blue", label = "Treasury")
plt.plot(years, put, color ="red", label = "Put")

plt.legend()

plt.show()