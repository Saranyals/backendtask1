import json,urllib.request
url= input("Enter the url:\n")
#url="https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

investrs=set([])
try:
    for i in range(1,len(data)+1):
        #print('Episode '+str(i)+"\n\n\n")
        for x in data['Episode '+str(i)]:
            s=x['investors'].replace('and',',')
           # print(l)
            s=s.split(',')
            #print(l)
            for i in range(len(s)):
                s[i]=s[i].strip('\n').lstrip().rstrip()
            #print(l[i])
            investrs=investrs.union(s)
           # print(invest)
    investrs.remove('')
    #print(invest)
    ab = {e:[] for e in investrs}
    for i in range(1,len(data)+1):
        for x in data['Episode '+str(i)]:
            sample=x['investors']
            for i in ab:
                if i in sample:
                    ab[i].append(x['product'].lstrip().rstrip().strip('\n'))
    for k in sorted(ab, key=lambda k: len(ab[k]), reverse=True):
        print (str(k)+"  : "+str(ab[k]))
        print("\n")
except (ValueError, KeyError, TypeError):
    print("JSON format error")
