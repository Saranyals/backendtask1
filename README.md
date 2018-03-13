# backendtask1
code with detailed descriptions:
url= input("Enter the url:\n")
# url is inputted from the user
response = urllib.request.urlopen(url)
# request to open the url and handles the response
data = json.loads(response.read().decode())
# reads and loads the data in the url and decodes it then stores to a variable
investrs=set([])
# unorder data type collection which is iteratable and has no duplicates which is done to use union(mathematical function) for sorting.
try: for i in range(1,len(data)+1):
# for loop runs from 1 to length of data+1 size
  for x in data['Episode '+str(i)]:   
# x= data[Episode 1] and the iteration goes on for all episodes
        s=x['investors'].replace('and',',')   
# replaces and with comma and s contains the investors name
        s=s.split(',')  
# splits the the name of the investors as individual. Ex: ['Lori Greiner ', ' Robert Herjavec']
        for i in range(len(s)):   
# loop runs upto length of s
            s[i]=s[i].strip('\n').lstrip().rstrip()    
# removes all ‘\n’ in leading and end of the string
# for loop ends
        investrs=investrs.union(s)  
# all investors name is union and created as a set
investrs.remove('')  
# Removes double quotes
ab = {e:[] for e in investrs}  
# loop runs through the set invest created by getting the name of each investors
for i in range(1,len(data)+1):    
# inner loop runs from 1 to length of data+1
    for x in data['Episode '+str(i)]: 
# loops through each episode
        sample=x['investors']  
# investors in original data is fetched
        for i in ab:
            if i in sample:   
# compares the value of original data (i) and created set invest(ab)
                ab[i].append(x['product'].lstrip().rstrip().strip('\n'))  
# appends the products of the investors
for k in sorted(ab, key=lambda k: len(ab[k]), reverse=true):   
# sorting function: sorts based on the length of investor’s product
    print (str(k)+"  : "+str(ab[k]))    
# prints the investors name whos has invested in maximum number and their product of investments.
    print("\n")
except (ValueError, KeyError, TypeError): print("JSON format error")
