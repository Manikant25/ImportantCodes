import math

def minimax(currDepth,nodeIndex,maxTurn,scores,targetDepth):

    if currDepth==targetDepth
        return scores[nodeIndex]


    if maxTurn:
        return max(minimax(currDepth+1,nodeIndex*2,False,scores,targetDepth),
                   minimax(currDepth+1,nodeIndex*2 +1, False,scores,targetDepth))
    else:
        return  min(minimax(currDepth+1,nodeIndex*2,False,scores,targetDepth),
                   minimax(currDepth+1,nodeIndex*2 +1, False,scores,targetDepth))
