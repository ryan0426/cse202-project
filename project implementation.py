#!/usr/bin/env python
# coding: utf-8

# In[32]:


import time
import sys
sys.setrecursionlimit(1500)

initialState = [
    [(1,0)],
    [(1,2)],
    [(0,0), (3,0), (0,2), (3,2)],
    [(1,3), (2,3), (0,4), (3,4)],
    [(1,4), (2,4)]
]
'''
#other initial state
initialState = [
    [(1,0)],
    [(1,3)],
    [(0,0), (3,0), (0,3), (3,3)],
    [(0,2), (1,2), (2,2), (3,2)],
    [(1,4), (2,4)]
]

initialState = [
    [(0,0)],
    [(2,1)],
    [(0,2), (1,2), (2,2), (3,2)],
    [(2,0), (3,0), (0,4), (3,4)],
    [(1,4), (2,4)]
]
'''
output = (1,3)


# In[33]:


def possibleNextStates(state):
    result = []
    size2_2 = state[0]
    size2_1 = state[1]
    size1_2 = state[2]
    size1_1 = state[3]
    blank = state[4]

    for (x,y) in size2_2:
        #check if (x,y) can move in 4 direction
        if (x-1,y) in blank and (x-1,y+1) in blank:
            s = [[(x-1,y)],size2_1,size1_2,size1_1,[(x+1,y),(x+1,y+1)]]
            result.append(s)
        if (x+2,y) in blank and (x+2,y+1) in blank:
            s = [[(x+1,y)],size2_1,size1_2,size1_1,[(x,y),(x,y+1)]]
            result.append(s)
        if (x,y-1) in blank and (x+1,y-1) in blank:
            s = [[(x,y-1)],size2_1,size1_2,size1_1,[(x,y+1),(x+1,y+1)]]
            result.append(s)
        if (x,y+2) in blank and (x+1,y+2) in blank:
            s = [[(x,y+1)],size2_1,size1_2,size1_1,[(x,y),(x+1,y)]]
            result.append(s)
            
    for i in range(len(size2_1)):
        #check if (x,y) can move in 4 direction
        (x,y) = size2_1[i]
        if (x-1,y) in blank:
            blank_state = blank.copy()
            idx = blank.index((x-1,y))
            blank_state[idx] = (x+1,y)
            s = [size2_2,[(x-1,y)],size1_2,size1_1,blank_state]
            result.append(s)
        if (x+2,y) in blank:
            blank_state = blank.copy()
            idx = blank.index((x+2,y))
            blank_state[idx] = (x,y)
            s = [size2_2,[(x+1,y)],size1_2,size1_1,blank_state]
            result.append(s)
        if (x,y-1) in blank and (x+1,y-1) in blank:
            s = [size2_2,[(x,y-1)],size1_2,size1_1,[(x,y),(x+1,y)]]
            result.append(s)
        if (x,y+1) in blank and (x+1,y+1) in blank:
            s = [size2_2,[(x,y+1)],size1_2,size1_1,[(x,y),(x+1,y)]]
            result.append(s)
            
    for i in range(len(size1_2)):
        #check if (x,y) can move in 4 direction
        (x,y) = size1_2[i]
        if (x-1,y) in blank and (x-1,y+1) in blank:
            size_state = size1_2.copy()
            size_state[i] = (x-1,y)
            s = [size2_2,size2_1,size_state,size1_1,[(x,y),(x,y+1)]]
            result.append(s)
        if (x+1,y) in blank and (x+1,y+1) in blank:
            size_state = size1_2.copy()
            size_state[i] = (x+1,y)
            s = [size2_2,size2_1,size_state,size1_1,[(x,y),(x,y+1)]]
            result.append(s)
        if (x,y-1) in blank:
            size_state = size1_2.copy()
            size_state[i] = (x,y-1)
            blank_state = blank.copy()
            idx = blank.index((x,y-1))
            blank_state[idx] = (x,y+1)
            s = [size2_2,size2_1,size_state,size1_1,blank_state]
            result.append(s)
        if (x,y+2) in blank:
            size_state = size1_2.copy()
            size_state[i] = (x,y+1)
            blank_state = blank.copy()
            idx = blank.index((x,y+2))
            blank_state[idx] = (x,y)
            s = [size2_2,size2_1, size_state,size1_1,blank_state]
            result.append(s)

            
    for i in range(len(size1_1)):
        #check if (x,y) can move in 4 direction
        (x,y) = size1_1[i]
        if (x-1,y) in blank:
            size_state = size1_1.copy()
            blank_state = blank.copy()
            size_state[i] = (x-1,y)
            idx = blank.index((x-1,y))
            blank_state[idx] = (x,y)
            s = [size2_2,size2_1,size1_2,size_state,blank_state]
            result.append(s)
        if (x+1,y) in blank:
            size_state = size1_1.copy()
            blank_state = blank.copy()
            size_state[i] = (x+1,y)
            idx = blank.index((x+1,y))
            blank_state[idx] = (x,y)
            s = [size2_2,size2_1,size1_2,size_state,blank_state]
            result.append(s)
        if (x,y-1) in blank:
            size_state = size1_1.copy()
            blank_state = blank.copy()
            size_state[i] = (x,y-1)
            idx = blank.index((x,y-1))
            blank_state[idx] = (x,y)
            s = [size2_2,size2_1,size1_2,size_state,blank_state]
            result.append(s)
        if (x,y+1) in blank:
            size_state = size1_1.copy()
            blank_state = blank.copy()
            size_state[i] = (x,y+1)
            idx = blank.index((x,y+1))
            blank_state[idx] = (x,y)
            s = [size2_2,size2_1,size1_2,size_state,blank_state]
            result.append(s)

    return result


# In[34]:


def isSearchEnd(state):
    size2_2 = state[0]
    for i in size2_2:
        if i == output:
            return True
        else:
            return False
    
    return False


# In[52]:


def bfs(state):
    global hasFoundSolution, step, start_time
    queue = []
    queue.append((state,0))

    while len(queue) != 0 and hasFoundSolution == False:

        step += 1
        
        s = queue.pop(0)
        
        if isSearchEnd(s[0]):
            hasFoundSolution = True
            print ("find solution!")
            end_time = time.time()
            print("time: %.9f" % (end_time - start_time))
            print("step: ", step)
            print("depth: ", s[1])
            return
        
        nextStates = possibleNextStates(s[0])
        
        for i in range(len(nextStates)):
            
            for j in nextStates[i]:
                j.sort()
                
            #make sure the next state is not visited before
            if nextStates[i] not in pastStates:
                
                pastStates.append(nextStates[i])

                #add the state in the queue
                queue.append((nextStates[i], s[1] + 1))

    return


# In[53]:


def dfs(s):
    global step, hasFoundSolution, start_time
    
    if(isSearchEnd(s[0])):
        print ("find solution!")
        hasFoundSolution = True
        end_time = time.time()
        print("time: %.9f" % (end_time - start_time))
        print("step: ", step)
        print("depth: ", s[1])
        return
        
    step += 1
    
    nextStates = possibleNextStates(s[0])
    
    
    for i in nextStates:
        
        for j in i:
            j.sort()
            
        if i not in pastStates:
            
            pastStates.append(i)
            
            dfs((i, s[1] + 1))
            
            if hasFoundSolution:
                return
            


# In[57]:


pastStates = []
maxDepth = 10
currentDepth = 0
hasFoundSolution = False
step = 0
start_time = time.time()

dfs((initialState, 0))


# In[ ]:


pastStates = []
maxDepth = 10
currentDepth = 0
hasFoundSolution = False
step = 0
start_time = time.time()

bfs(initialState)


# In[56]:
