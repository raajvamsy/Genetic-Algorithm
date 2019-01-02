import sys
import random
import os

data = {}
pop =0
char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mutationrate = 0.1
sys.setrecursionlimit(10000)


#Population
def population(data,userdata):
    global pop
    pop+=1

    for j in range(random.randint(0,1000)):
        text=""
        for i in range(0,len(userdata)):
            text+=char[random.randint(0,len(char)-1)]
        data[text]=0
    fitness(data,userdata)
#print(population())
#Fitness
def fitness(data,userdata):
    st = []
    for key in data.items():
        st.append(key[0])
    fit = []
    for i in range(len(data)):
        fit.append(0)
    for i in range(len(data)):
        t=c=0
        for j in range(len(st[i])):
            if st[i][j] == userdata[j]:
                t = t + 1
            if st[i].count(st[i][j]) == userdata.count(userdata[j]):
                c = c + 1
            c = c / st[i].count(st[i][j])
        t = t / len(st[i])
        fit[i] = fit[i] + t + c

    for i in range(len(fit)):
        data[st[i]]=fit[i]

    crossover(data,userdata)

#Crossover
def crossover(data,userdata):
    global mutationrate,pop,char
    d = data
    data = sorted(data.items(),key=lambda x:x[1],reverse=True)
    if(data[0][0]==userdata):
        print(data[0][0])
        return data[0][0]
    else:
        mutation = []
        for i in range(int(mutationrate * 100)):
            mutation.append(1)
        for i in range(int(100 - mutationrate * 100)):
            mutation.append(0)
        m = random.choice(mutation)
        child = ""
        l = []
        for i in range(pop):
            for j in range(int(data[i][1] * 10)):
                l.append(data[i][0])
        #print(l)
        c1 = random.choice(l)
        c2 = random.choice(l)
        child = c1[int(len(c1) / 2):] + c2[-(int(len(c2) / 2)):]
        child = list(child)
        if m == 1:
            child[random.randint(0, len(child) - 1)] = random.choice(char)
        child = ''.join(child)
        print(str(data[0][0])+"-pop:"+str(pop))
        if (child != userdata):
            d[child] = 0
            data = d
            population(data, userdata)
        else:
            print("done")
            return child
userdata = "RAAJ"
population(data,userdata)
