global dic
dic={}
default=["...","..x",".x.",".xx","x..","x.x","xx.","xxx"]
def getpattern(x):    
    if x==0:
        return dic
    elif x==1: 
        dic[default[0]]="x"
        return dic  
    else:
        i=0
        while True:
            if 2**i==x:
                dic[default[i]]="x"    
                return dic    
            elif 2**i>x:
                a=i-1
                dic[default[i-1]]="x"
                getpattern(x-(2**a)) 
                return dic      
            else:
                i=i+1               

def cellular_automaton(string, pattern, generation):
    global dic
    dic={}
    dic_pattern=getpattern(pattern)
    for s in default:
        if s not in dic:
            dic[s]="."

    new_string=string[-1]+string+string[0]
    for m in range(1,generation+1):
        new_new_string=""
        for k in range(0,len(string)):
            if new_string[0:3] in dic_pattern:
                new_new_string=new_new_string+dic_pattern[new_string[0:3]]
                new_string=new_string[1:]
        new_string=new_new_string[-1]+new_new_string+new_new_string[0]
    
    return new_new_string
    
print cellular_automaton('.x.x.x.x.', 17, 2)

print cellular_automaton('.x.x.x.x.', 249, 3)

print cellular_automaton('...x....', 125, 1)

print cellular_automaton('...x....', 125, 2)

print cellular_automaton('...x....', 125, 3)

print cellular_automaton('...x....', 125, 4)

print cellular_automaton('...x....', 125, 5)

print cellular_automaton('...x....', 125, 6)

print cellular_automaton('...x....', 125, 7)

print cellular_automaton('...x....', 125, 8)

print cellular_automaton('...x....', 125, 9)

print cellular_automaton('...x....', 125, 10)

print cellular_automaton('....................x....................', 126, 100)
