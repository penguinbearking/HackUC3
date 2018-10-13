import random
import numpy
import math

def projections(historicaldata, predictionlength):
  def std(items):
    square=0
    for i in items:
      square+=(i-(sum(items)/len(items)))**2
    return math.sqrt((1/len(items))*square)
    
  n=predictionlength
  k=int(1000/n)
  iterProject=[]
  projections=[]
  projectionList=[]
  actualProjectionList=[]
  stdevs=[]
  bearProjections=[]
  bullProjections=[]
  bullPrices=[]
  bearPrices=[]
  deviations=[]
  for i in range(n):
    projections.append(0)
    actualProjectionList.append([])
    deviations.append([])
  for j in range(k):
    prices = historicaldata
    newprices = prices
    wins=0
    losses=0
    for item in range(len(prices)-1):
      if prices[item+1]>prices[item]:
        wins+=1
      else:
        losses+=1
    iterProject=[]
    for i in range(n):
      winStreak=0
      loseStreak=0
      winProb=0
      loseProb=0
      prediction=prices[len(prices)-1]
      winAmount=[]
      lossAmount=[]
      for item in range(len(prices)-1):
        if newprices[item+1]>newprices[item]:
          if winStreak>0:
            winProb+=1.0/float(wins)
          winStreak+=1
          loseStreak=0
          winAmount.append(float(newprices[item+1])/float(newprices[item]))
        else:
          if loseStreak>0:
            loseProb+=1.0/float(losses)
          winStreak=0
          loseStreak+=1
          lossAmount.append((newprices[item+1])/(newprices[item]))
      if winStreak>0:
        if random.uniform(0,1)<winProb:
          prediction*=random.gauss((sum(winAmount))/(len(winAmount)),std(winAmount))
          wins+=1
        else:
          prediction*=random.gauss((sum(lossAmount))/(len(lossAmount)),std(lossAmount))
          losses+=1
      else:
        if random.uniform(0,1)<loseProb:
          prediction*=random.gauss((sum(lossAmount))/(len(lossAmount)),std(lossAmount))
          losses+=1
        else:
          prediction*=random.gauss(float(sum(winAmount))/float(len(winAmount)),std(winAmount))
          wins+=1
      newprices.append(prediction)
      iterProject.append(prediction)
    projectionList.append(iterProject)
    for item in range(len(iterProject)):
      projections[item]+=float(iterProject[item])/float(k)
  projections.pop(len(projections)-1)
  for i in range(n-1):
    for j in range(k):
      actualProjectionList[i].append(projectionList[j][i])
      deviations[i].append(abs(1-float(projectionList[j][i])/float(projections[i])))
  for i in range(n-1):
    stdevs.append(sum(deviations[i])/len(deviations[i]))
  for i in range(len(projections)):
    bullProjections.append(projections[i]*((stdevs[i])+1))
    bearProjections.append(projections[i]*(1-(stdevs[i])))
  print(projections)
  print(bullProjections)
  print(bearProjections)
  return bearProjections
#print (bearProjections)
