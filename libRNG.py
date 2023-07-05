def maxCount(res, nQubit):
    maxF = (nQubit)*"0"
    for i in res:
        if int(res[i]) > int(res[maxF]):
            maxF = i            
    return maxF

def bin2Dec(bin):
    return int(bin,2)

#Not used yet
def XY(res):
    xData = []
    yData = []

    for i in res:
        yData.append(int(res[i]))
        xData.append(int(i))
    return (xData, yData)
