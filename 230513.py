#print 옆에 주석은 어떻게 출력되는지야!
#열심히 쓰고잇으니까 참고해 히히
#안온놈들을 위한 정성이다 ㅎㅋ

#리스트 특징
#새로운 항목 추가 / 삭제 가능
#인덱스를 가짐, 인덱스 번호는 0부터 시작!
#숫자 / 문자열 모두 가능 (같은 자료형일 필요 없음)

number = [1,2,3,4,5]
print(number) #[1, 2, 3, 4, 5]
print(number[2]) #3
print(number[-1]) #5

#실습 1 - 친구이름 5개를 리스트로 만들어보자!
names = ["심아현", "김화응", "김유림", "이선우", "임예섭"]
print(names) #['심아현', '김화응', '김유림', '이선우', '임예섭']

#리스트와 조건문
#리스트 슬라이싱 - 문자열과 동일하게 인덱스로 슬라이싱 가능

shop = ["반팔", "청바지", "이어폰", "키보드", "마우스"]

#인덱싱
print(shop[0]) #반팔
#슬라이싱
print(shop[0:2]) #['반팔', '청바지']
#슬라이싱 이렇게하면 인덱스 0부터 2에서 1뺀것까지 가져오는거임다
print(shop[2:]) #['이어폰', '키보드', '마우스']
#이러면 인덱스 2부터 끝까지 가져오는거

#참고
#https://codetorial.net/tips_and_examples/list_slicing.html
#원래 코딩 공부할땐 더 찾아가면서 하고 쌤이 하라는거 말고 더 바꿔가면서 해야 늘어
#사실 재밋기도 하고

#리스트 연산
#더하기 + / 반복 * / 길이 len() 
a = [1,2,3]
b = [6,7]
print(a+b) #[1, 2, 3, 6, 7]
print(len(a)) #3 이건 리스트 길이 알려주는거!
print(a*4) #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 값 수정
#인덱스로 접근해 값 수정하기
#주의) 리스트 길이를 넘는 인덱스로 요소에 접근하면 IndexError 발생

#리스트 함수
#정렬
num = [3,1,5,2]

#sort() 말그대로 순서대로 정렬하는거!
num.sort()
print(num) #[1, 2, 3, 5]
#reverse() 이건 뒤집어서 순서대로!
num.reverse()
print(num) #[5, 3, 2, 1]

hihi = ["임","예","섭","바","보"]
hihi.sort()
print(hihi) #['바', '보', '섭', '예', '임'] 한글순서로 정렬이야
#솔트 함수는 반환값이 없는 함수야
print(num.sort()) #Nome

#리스트 함수 추가 / 삭제
#요소이름으로 추가/삭제
#append() : 맨 마지막에 요소 추가
#remove() : 리스트에서 첫 번째로 나오는 요소 삭제

print(num.append(4)) #None 역시 반환값이 없어
num.append(4)
print(num) #[1, 2, 3, 5, 4, 4]

#요소 번호로 추가/삭제 
#원하는 위치에 추가, 삭제 가능
#pop() : 맨 마지막요소 삭제     푸쉬팝은 알고리즘에서도 많이 쓰여
#del list_name[idx] : idx번째 요소를 삭제

number.insert(10,11)
print(number) #[1, 2, 3, 4, 5, 11]

number.pop()
print(number) #[1, 2, 3, 4, 5]
number.pop(3)
print(number) #[1, 2, 3, 5]

del number[2]
print(number) #[1, 2, 5]
del number[2 :]
print(number) #[1, 2]

#리스트 함수 위치찾기
#만약에 리스트 갯수가 100개가 넘어간다...면 위치찾는게 필요하겟져
#index(item)
#리스트함수 - 개수세기
#중복된 상품명, 동명이인도 상품코드나 출석 번호가 다르면 다른것으로 판단
#count(item) : 같은 이름 가진 요소 개수 세기

kkaaak = ["살", "려","주","세","요","오","오"]
print(kkaaak.index("오")) #5

#실습 2 : 다음과 같은 리스트가 있을 때 결과를 출력해보세요
rainbow = ['red','orange','yellow','green','blue','indigo','purple']
#1. 2번 인덱스 값 출력
#2. 알파벳 순서로 정렬한 값 출력
#3. 좋아하는 색 맨 마지막에 추가하기
#4. 3~6번째 값 삭제하기










#1
print(rainbow[2])
#2
rainbow.sort()
print(rainbow)
#3
rainbow.append("red")
print(rainbow)
#4
del rainbow[3:6]
print(rainbow)


#조건문
#Boolean 자료형 불리언/불
#True False 두가지
#비교연산자를 사용해 불이 나오는 결과를 만듦.
#None, 숫자 0, 빈문자열/리스트 등 모두 False로 변환됨
print(bool(0)) #False
print(bool(2)) #True
print(bool(-1)) #True
print(bool(None)) #False
print(bool()) #False

#비교연산자
# == 같다
# != 다르다
#나머지는 상식대로
#파이썬은 3 < x < 5 이런게 됨
#(자스같은건 안되어서 3 < x && x < 5 이케써야댐 ㅜ)

#집가고싶
#다
#아아아아ㅏ아아아악

#논리연산자
#Boolean 데이터끼리 논리 연산자 사용ㄱㄴ
#not 부정
#and 그리고 -> 둘다 참이어야 참, 하나라도 거짓이면 거짓.
#or 또는 -> 둘 중 하나라도 참이면 참, 둘다 거짓이면 거짓.

#실습하기가 귀찮습니다아아아아아아악...

#if 조건문
#만약에 

x = input("숫자를 입력하시라요 : ")
x = int(x)
if x > 10 :
    print("10보다커요잉")
else :
    print("10보다 작아요잉")

#실습 3 : 숫자를 입력받아 홀짝 구분하기







num1 = input("숫자를 입력하세요잉 : ")
try :
    num1 = int(num1)
    if num1 % 2 == 0 :
        print("짝수입니다잉")
    else :
        print("홀수입니다잉")

except :
    print("이것은 숫자가 아닌디유")

#이건 내가 걍 한건데 try except는 예외처리문이고 배운건 아님 궁금하면 이거 참고해
#https://dojang.io/mod/page/view.php?id=2398
#대충 설명하자면
#num1을 입력받아서 숫자로 변환해야 홀짝인지 비교할수 있지?
#근데 문자를 입력하면 에러가 나. 숫자로 변환할수 없으니까!
#그래서 예외처리문이 필요했어!
#일단 입력을 받아서 값을 저장하고
#try문에서 숫자로 바꿔 근데 try문에서 에러가 나면 except쪽으로 넘어가는거야
#하튼 그런거야 ^^

#if-else 문 
#와 위에서 벌써 썼는데요
#else문은 if에 해당하지 않을때..
#elif도 있어 이건 다른조건

sunwoo = "바보"
if sunwoo == "바보" :
    print("이선우는 바보입니당 ㅅㄱ")
else : 
    print("그럴리가 없는데")

#실습예제 따라치기 귀찮지만 해줄게
#근데 다른거 해야지

mon = int(input("몇월인지 입력하세요 : "))
def season(mon) : #이건 밑에 코드를 함수로 만든거야 또쓸라고 함수로 만들어버림
    if 3<= mon <= 5 :
        print("봄")
    elif 6<= mon <= 8 :
        print("여름")
    elif 9<= mon <= 11 :
        print("가을")
    elif mon==12 or 1<= mon <= 2 :
        print("겨울")
    else :
        print("입력값을 다시한번 확인해주세요.")

#원래 함수는 코드 끝이나 첫머리에 몰아놔
season(mon)

#근데 실제 이번달을 불러오는것도 낫배드...?
#날짜 / 시간 모듈을 불러오면 댐 (역시 내맘대로 쓰는거임 ㅋㅋ)
#time도 있지만 이건 복잡하니 datetime으로 써봅시다
import datetime as dt #이렇게 모듈을 불러오고
#(datetime이란 모듈을 불러올껀데 이걸 dt로 사용한단 뜻)
now = dt.datetime.now() #now라는 변수에 현재를 저장한거야
print(now) #2023-05-13 11:37:54.593482
season(now.month) #봄 (위에 저장된거중에 현재 날짜를 가져온거야)
# 참고 : https://datascienceschool.net/01%20python/02.15%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%82%A0%EC%A7%9C%EC%99%80%20%EC%8B%9C%EA%B0%84%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html

#사실 주어진 실습이 잇지만 하고싶은걸 공부하는 케이스
#하지만 나한테는 파이썬 어디서 교육받을때마다 맨날 해본거라고 진짜 ㅜ

#이번엔 제대로 하는
#실습 4
#교통비를 낼 때 나이와 결제 방법에 따른 금액을 출력하세요
#ㅇㄴ 요즘에 현금결제 안되는데 굳이 현금이요?

age = int(input("나이를 입력하세요 : "))
if age < 8 or age >= 75:
    print("무료입니다.")
elif 8<= age < 14 :
    print("요금은 450원 입니다.")
else :
    sudan = input("결제수단은? 카드/현금 : ")
    if 14 <=age <20 :
        if sudan == "카드" :
            print("요금은 720원 입니다.")
        else :
            print("요금은 1000원 입니다.")
    else :
        if sudan == "카드" :
            print("요금은 1200원 입니다.")
        else :
            print("요금은 1300원 입니다.")
