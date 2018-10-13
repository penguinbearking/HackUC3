import random
import numpy
import math

def std(items):
    square=0
    for i in items:
      square+=(i-sum(items)/len(items))**2
    return math.sqrt((1/len(items))*square)

n=100
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
    prices = [209.59,210.88,210.65,213.8,207.97,206.11,205.96,206.72,206.64,208.26,209.17,208.43,207.53,205.79,203.49,204.25,206.43,207.39,209.81,210.29,209.33,211.78,213.96,212.79,212.96,213.47,214.56,216.24,215.92,215.97,217.4,219.76,222.45,219.76,222.22,224.62,224.34,223.79,224.04,226.77,226.92,225.42,224.38,224.34,225.13,225.57,226.58,231.69,232.54,233.19,236.55,234.67,235.78,235.6,236.54,233.34,235.33,234.72,237.3,238.97,238.9,235.14,235.71,232.47,228.69,228.63,233.52,233.75,236.44,235.97,237.28,237.73,242.22,243.03,242.38,244.74,242.42,241.75,242.02,242.29,243.08,240.51,235.52,235.16,234.79,237.73,237.24,236.08,237.13,237.85,237.58,236.41,237.54,234.43,232.76,233.2,236.11,235.45,240.12,241.35,244.75,246.63,247.98,247.35,245.04,245.51,243.94,245.65,245.67,239.96,239.58,241.13,241.49,245.73,246.13,244.35,244.99,244.06,247.58,245.26,247.03,248.93,248.74,249.6,250.84,252.04,252.7,251.79,244.05,241.59,242.82,243.01,242.22,238.11,233.66,235.01,236.07,236.36,236.24,238.18,238.67,237.95,240.22,236.01,234.55,236.59,236.12,234.91,235.99,237.03,236.84,237.04,236.88,240.68,243.34,245.67,246.25,247.15,247.38,246.51,249.77,249.67,250.19,247.81,252.84,253.3,252.84,252.93,248.52,250.08,253.83,250.47,248.14,247.67,247.06,235.18,230.67,231.94,231.72,231.68,232.31,232.21,234.93,235.67,236.28,231.83,232.23,229.91,231.32,233.6,233.92,233.71,234.78,234.41,236.68,235.85,235.48,235.91,235.37,238.8,239.53,238.84,235.97,235.88,236.26,239.28,238.26,238.77,239.26,240.94,243.71,243.98,245.8,246.2,246.58,245.87,245.77,246.13,247.08,246.64,243.02,244.5,243.21,236.78,237.66,242.05,245.86,247.45,248.17,248.77,249.22,249.05,254,253.85,253.04,251.17,251.16,249.28,250.96,248.17,247.35,248.21,250.04,247.56,246.78,249.73,248.75,246.34,246.75,246.92,244.67,243.37,242.17,246.45,252.19,252.78,255.33,257.28,258.73,260.3,259.95,262.64,265.49,266.28,269.34,269.04,267.84,273.91,270.1,269.61,273.75,275.4,274.24,274.08,276.45,275.99,279.64,281.16,280.04,278.16,275.07,277.54,275.62,279.7,285.49,285.42,285.57,285.48,282.38,282.88,284,282.96,284.2,283,284.12,288.62,290.52,290.66,288.3,290.86,290.31,291.22,289.89,288.23,292.47,292.78,294.08,298.17,301.16,301.64,300.38,300.93,296.13,289.2,291.7,292.39,293.63,300.41,301.95,296.69,297.26,292.86,292.49,285.62,279.16,284.44,286.91,286.09,293.07,287.19,286.82,281.52,281.83,282.51,284.57,288.36,288.03,289.36,295.34,295.47,294.71,293.37,291.57,293.3,293.98,294.24,287.43,286.65,279.62,278.21,280.17,282.16,289.11,288.73,290.76,290.1,289.83,288.46,293.47,295.09,293.45,296.72,297.28,297.47,298.73,301.62,303.14,304.76,304.81,305.69,306.97,309.65,308.43,306.86,308.96,307.16,307.9,304,302.94,305.63,304.92,307.4,308.29,307.52,308.37,307.63,310.68,310.42,312.7,314.59,311.39,308.55,308.47,307.81,309.27,310.65,312.33,315.65,318.05,318.66,317.57,316.23,318.45,322.09,323,328,333.33,332.39,334.65,333.99,334.11,329.25,329.83,334.84,335.9,333.33,336.77,334.57,331.38,327.04,329.8,323.4,321.68,320.21,316.7,313.56,313.92,317.13,321.98,323.08,317.74,314.86,314.93,314.86,310.54,319.5,321.19,319.72,320.16,323.2,321.69,321.83,327.33,328.07,328.08,319.22,318.52,314.16,311.07,309.39,314.52,305.23,298.08,282.7,224.84,236.83,258.38,248.25,248.22,227.67,233.19,233.28,244.77]
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
#return bearProjections
#print (bearProjections)
