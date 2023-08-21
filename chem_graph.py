import math
import numpy as np
import matplotlib.pyplot as plt

print('구하려는 값은 00 으로 입력해주세요.')
bangamgis = {
    'Po' : 102,# 폴로늄
    'U' : 2.34 * 107, # 우라늄
    'Pu' : 8.00 * 107, # 플루토늄
    'C' : 5730 # 탄소   
}

print('사용 가능 원소 ', bangamgis.keys())
No = float(input('초기 모원소의 양 : '))
T = input('사용 원소 또는 반감기를 직접 입력하세요 : ')

if T in bangamgis :
  T = bangamgis.get(T)
else :
  T = float(T)

t = float(input('흐른 시간 : '))
Ntp = float(input('남아있는 모원소의 양 : '))

if Ntp == 00 :
  Ntp = No * ((1/2)**(t/T))

elif No == 00:
  No = Ntp / ((1/2)**(t/T))

elif t == 00 :
  t = T * float(math.log(0.5, (Ntp / No)))
  
elif T == 00 :
  T = t / float(math.log(0.5, (Ntp / No)))

Ntd = No - Ntp # 자원소
print('---------- \n계산결과 \n')
print(f'초기 모원소(No) : {No}, 반감기(T) : {T}, \n흐른 시간(t) : {t}, \n모원소 양(Ntp) : {Ntp}, \n자원소 양(Ntd) : {Ntd}')
print('\n------------\n')

print('그래프')
# 그래프 그리기
# plt.plot(x축,y축, label=그래프이름)
t=np.arange(0,3*(10**11),1000000)
Ntp = No * ((1/2)**(t/T))
Ntd = No - Ntp

print(Ntp,'\n',Ntd)

plt.plot(t,Ntp, label='parent element')
plt.plot(t,Ntd, label='daughter element')


plt.xlabel('t')
plt.ylabel('Ntp / Ntd')
plt.legend() # 범례표시
plt.grid() # 보조선
# plt.xlim(0,500000000) # x축 간격
plt.show()