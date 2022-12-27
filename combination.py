def facto(n) :
  i=0
  sum = 1
  while n-i >= 1 :
    sum *= (n-i)
    i+=1
  return sum

def combi(n,r) :
 sum2 = facto(n) / (facto(n-r)*facto(r)) 
 return sum2
  
n, r=input("nCr의 n과 r을 순서대로 입력하세요 :").split()
n = int(n)
r = int(r)

if n < r:
  print("error")
else :
 print(combi(n,r))
