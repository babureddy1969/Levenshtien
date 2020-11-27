from Levenshtein import distance
import random,json
import threading,time
from datetime import datetime

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
refs=[r.replace('\n','') for r in open('refs.txt').readlines() ]
x={}
for i,r in enumerate(refs):
    refs[i]="".join([a for a in r if a in alpha or a in num])
    x[r]=refs[i]
refs=list(set(sorted([r.strip() for r in refs if len(r.strip())>0],reverse=True)))

ref_len={}
for r in refs:
    ref_len[len(r)] = ref_len.get(len(r),0)+1
dupes={}
def findDupes(name,min,max,refs):
    group_number=1
    for i in range(min,max):
        for j in range(len(refs)):
            str1 = refs[i]
            str2 = refs[j]
            if str1==str2:continue
            d = distance(str1,str2)
            if d < 2: 
                # print (name,str1,str2,d)
                dupes[str1] =dupes.get(str1,[])+[str2]
                # print(name,i,max)
# refs=refs[:10000]                
# for max_threads in range(10,101,10):
ref_len = sorted(ref_len.keys(),reverse=True)
print(ref_len)
while len(ref_len)>1:
    maxlen = ref_len.pop(0)
    r = [r for r in refs if len(r) in [maxlen,maxlen-1 ] ]
    # print(maxlen,len(refs))
    if (len(r)<=1000) : 
        start = datetime.now()
        findDupes('x',0,len(refs),r)
        print(maxlen,len(r),end-start)
        continue
    max_threads=10
    t=[]
    start=datetime.now()
    y=int(len(r)/max_threads)
    for i in range(max_threads):
        min=i*y
        max=min+y
        x=threading.Thread(target=findDupes,args=('t'+str(i),min,max,r))
        x.start()
        x.join()
        t+=[x]
    end=datetime.now()
    print(maxlen,len(r),max_threads,end-start)