# 파이썬 기초

# 주석 ctrl + /
# 코드 실행
# 1) ctrl + enter: 커서의 위치가 그대로
# 2) alt + enter: 새로운 셀로 이동(새로 셀을 만듦)
# 3) shift + enter: 새로운 셀로 이동(기존 만들어진 셀)

# 출력을 해주는 함수
print("안녕 파이썬")

print("안녕"*10)

# 표현식
23
"Hello"
1+2
# + : 연산자

# 문장: 표현식이 모여서 실행할 수 있는 코드
# 한줄의 코드
a = 1+2

a

# 프로그램: 문장이 모여서 만들어진 코드

## 키워드 & 식별자

# 키워드 확인하는 방법
import keyword
print(keyword.kwlist)

# 식별자
student_name
_class
first name => first_name

## 연산자

# 값과 값 사이에 존재 + 기능
# 사칙연산
1+2

## print

print("이름")

print("이름A")
print("이름B")

print("이름A")
print()
print("이름B")

print("이름A", "이름B")

# 자료형

# 자료형 확인
type("배고파") # str = string 문자열

type(23) # int = integer 정수 = 소수점이 없는 숫자

type(2.3) # float 실수 = 소수점이 있는 숫자

type(True) # bool = boolean 불 = 논리형 = 참/거짓

## 문자열

print("안녕")
print('안녕')

# 문자열 안에서 따옴표를 사용하는 경우
print(""안녕"이라고 말해봐")

# 위의 에러 수정
print('"안녕"이라고 말해봐')

print("'안녕'이라고 말해봐")

### 이스케이프 문자

# 역슬래시(\) 와 함께 쓰는 문자
print("\"안녕\"이라고 말해봐")

print('\'안녕\'이라고 말해봐')

# 줄바꿈 \n
print("동해물과 백두산이\n마르고 닳도록")

# 탭 \t
print("안녕\t안녕")

# 역슬래시 \\
print("\\\\")

### 여러 줄의 문자열

print("하나~~~~~\n둘~~~~~\n셋~~~~~\n넷~~~~~~")

print("""하나~~~~~
둘~~~~~
셋~~~~~
넷~~~~~~""")

print("""
하나~~~~~
둘~~~~~
셋~~~~~
넷~~~~~~
""")

print("""\
하나~~~~~
둘~~~~~
셋~~~~~
넷~~~~~~\
""")

### 문자열 연산자

# + : 문자열 연결 연산자 = 합쳐주기
print("안녕"+"하시렵니까?")
print("안녕"+"!!!")
print("안녕"+1)

print("안녕"+"1")

# * : 문자열 반복 연산자 = 반복
print("안녕"*5)

print(5*"안녕")

### 인덱스 & 인덱싱

# 안녕하세요
# 1 2 3 4 5 => 원인덱스 = 보통 숫자 세는 방식
# 0 1 2 3 4 => 제로인덱스 = 파이썬 숫자 세는 방식
print("안녕하세요"[0])

print("안녕하세요"[1])

print("안녕하세요"[2])

print("안녕하세요"[3])

print("안녕하세요"[4])

print("안녕하세요"[5])

# 안녕하세요
# 1 2 3 4 5
# -5 -4 -3 -2 -1
print("안녕하세요"[-5])

print("안녕하세요"[-4])

print("안녕하세요"[-3])

print("안녕하세요"[-2])

print("안녕하세요"[-1])

### 슬라이싱

# 인덱스 범위 지정 = 슬라이싱
# [시작번호:끝번호]
# 파이썬은 끝번호를 포함하지 않음
# 안녕하세요
# 0 1 2 3 4
# 안녕 => 0:1 => 0:1+1 => 0:2
print("안녕하세요"[0:1+1])

print("안녕하세요"[0:2])

# 하세요 => 2:4 => 2:4+1 => 2:5
print("안녕하세요"[2:4+1])

print("안녕하세요"[2:5])

# 안녕
# 시작번호 생략 => [:1+1] = [:2] => 처음부터~
print("안녕하세요"[:1+1])
print("안녕하세요"[:2])

# 하세요
# 끝번호 생략 => [2:] => 끝까지~
print("안녕하세요"[2:])

### 문자열의 길이

# length 문자열 길이 반환 return
print(len("안녕하세요")) # = print(5)

## 숫자

# 정수
print(23)

print(type(23)) # int = integer 정수 = 소수점이 없는 숫자

# 실수
print(2.3)

print(type(2.3)) # float 실수 = 소수점이 있는 숫자

### 사칙연산자

print(3+2)
print(3-2)
print(3*2)
print(3/2)

# 나누기
print(3/2) # 실수
print(3//2) # 몫 = 정수
print(3%2) # 나머지 = 정수

# 제곱
2**2

2**3

2**4

### 우선순위

2+2*2

2+(2*2)

2+2-2*2/2*2

2+2-(((2*2)/2)*2)

5+3*2

(5+3)*2

### 숫자와 문자열 연산

number = 4
string = "랑해"
print(number + string)

number = "4"
string = "랑해"
print(number + string)

### 문자열의 우선순위

print("안녕"+"하세요")

print("안녕"+"하세요"*3)

print("안녕"+("하세요"*3))

print(("안녕"+"하세요")*3)

# 변수

# 변수 생성
pi = 3.14

# 변수 확인
print(pi)

# 변수 사용
print(pi + pi) # 3.14 + 3.14

## 연산

# 사칙연산
print(pi+pi)
print(pi-pi)
print(pi*pi)
print(pi/pi)

print(pi//2) # 몫
print(pi%2) # 나머지

# 제곱
print(pi**2)
print(pi**3)
print(pi**4)

# 원의 둘레 = 2*pi*r
# 원의 넓이 = pi*r*r
pi = 3.14
r = 10
print("원의 둘레: ", 2*pi*r)
print("원의 넓이: ", pi*r*r)

## 복합대입연산자

# += <= 숫자
no = 10
no += 1 # 10 + 1 = 11 = no
no += 1 # 11 + 1 = 12 = no
no += 1 # 12 + 1 = 13 = no
print(no)

# += <= 문자 (+, *)
string = "안녕"
string += "!" # 안녕 + ! = 안녕! = string
string += "!" # 안녕! + ! = 안녕!! = string
string += "!" # 안녕!! + ! = 안녕!!! = string
print(string)

## 사용자입력

# 사용자 입력 값을 반환
input("문자를 입력하세요> ")

input("숫자를 입력하세요> ")

# 문자열
var1 = input("문자를 입력하세요> ")
print(type(var1))

# 숫자
var2 = input("숫자를 입력하세요> ")
print(type(var2))

# bool
var3 = input("bool를 입력하세요> ")
print(type(var3))

no = input("정수를 입력하세요> ")
print("계산 결과: ", no + 10)

## 캐스트 함수

# 정수로 변환 int()
input_a = input("첫번째 정수를 입력하세요> ")
input_b = input("두번째 정수를 입력하세요> ")
int_a = int(input_a)
int_b = int(input_b)
print("문자열 = ", input_a + input_b)
print("정수 = ", int_a + int_b)

input_a = input("첫번째 정수를 입력하세요> ")
input_b = input("두번째 정수를 입력하세요> ")
int_a = float(input_a)
int_b = float(input_b)
print("문자열 = ", input_a + input_b)
print("정수 = ", int_a + int_b)

a = int("23")
b = float("2.3")
print(type(a))
print(type(b))

## 숫자를 문자로 변환

# str()
a = str(23)
b = str(2.3)
print(type(a))
print(type(b))

## ValueError

# 1) 숫자가 아닌 값을 숫자로 변환하는 경우
int("안녕")

# 2) 실수를 정수로 변환하는 경우
int("2.3")

## m => cm 변환 프로그램

# 1 m = 100 cm
meter = input("키(m)를 입력하세요> ")
meter = float(meter)
height = meter * 100
print(meter, "m 는 cm 로 변환하면 ", height, "cm 입니다.")

# inch 를 cm 로 변환하는 프로그램
# 1 inch = 2.54 cm
inch = input("inch 를 입력하세요> ")
inch = float(inch)
cm = inch * 2.54
print(inch, "inch 는 cm 로 변환하면 ", cm, "cm 입니다.")

#
#
#
# 함수

## format

# 숫자를 문자열로 변환하는 함수
a = "{}".format(23)
print(a)
print(type(a))

"유퀴즈 상금 {} 만원".format(100)

"{} {} {}".format(1,2,3)

"{} {} {}".format(1,2)

"{} {} {}".format(1,2,3,4)

"{}".format(2.3)

"{} {} {}".format(1,"안녕",True)

### 정수형

a = "{:d}".format(23) # 정수
b = "{:5d}".format(23) # 자리수 & 남은 자리를 빈칸으로 채움
c = "{:05d}".format(23) # 자리수 & 남은 자리를 0을 채움
d = "{:05d}".format(-23) # 자리수 & 한자리 - 기호 & 남은 자리를 0을 채움
print(a)
print(b)
print(c)
print(d)

a = "{:+d}".format(23) # 양수 기호와 함께 출력
b = "{:+d}".format(-23) # 음수, 무조건 - 기호
c = "{: d}".format(23) # 양수 기호를 생략해서 출력
d = "{: d}".format(-23) # 음수, 무조건 - 기호
print(a)
print(b)
print(c)
print(d)

a = "{:+5d}".format(23) # 자리수 & 숫자 바로 앞에 기호
b = "{:+5d}".format(-23) #
c = "{:=+5d}".format(23) # 자리수 & 맨 앞에 기호 & 남아있는 자리를 빈칸으로 채움
d = "{:=+5d}".format(-23) #
e = "{:=+05d}".format(23) # 자리수 & 맨 앞에 기호 & 남아있는 자리를 0으로 채움
f = "{:=+05d}".format(-23) #
print(a);print(b);print(c);print(d);print(e);print(f)

"{:+05d}".format(23) # = 사용할 필요 없음

### 실수형

a = "{:f}".format(23.45) # 실수
b = "{:15f}".format(23.45) # 자리수 & 남은 자리를 빈칸으로 채움
c = "{:+15f}".format(23.45) # 자리수 & 한자리 + 기호 & 남은 자리를 빈칸으로 채움
d = "{:+015f}".format(-23.45) # 자리수 & 한자리 - 기호 맨앞에 & 남은 자리를 0을 채움
print(a);print(b);print(c);print(d)

"{:=+015f}".format(-23.45) # = 사용할 필요 없음

a = "{:15.3f}".format(23.456)
b = "{:15.2f}".format(23.456)
c = "{:15.1f}".format(23.456)
d = "{:15.1f}".format(23.45) # 5 보다 커야 반올림
e = "{:15.1f}".format(23.46)
print(a);print(b);print(c);print(d);print(e)

"{:15.0f}".format(2.5)

"{:15.0f}".format(3.5)

"{:15.0f}".format(4.5)

"{:15.0f}".format(2.5123)

"{:15.0f}".format(3.51111)

### 의미가 없는 소수점 제거

a = "{:g}".format(23.450)
b = "{:g}".format(23.40)
c = "{:g}".format(23.0)
print(a);print(b);print(c)

## f 문자열 (참고만 할 것)

"{}".format(23)

f"{23}"

"{}".format(2 + 3)

f"{2+3}"

# format() 함수 사용하는 것이 더 좋은 경우
# 1) 문자열이 많을 때
mc = "유재석"
reward = 100
"""\
유퀴즈 프로그램은 다양한 사람을 만나서 이야기하는 프로이다.
엠씨는 {}이고, 퀴즈를 맞추면 상금 {} 만원을 준다.\
""".format(mc, reward)

mc = "유재석"
reward = 100
f"""\
유퀴즈 프로그램은 다양한 사람을 만나서 이야기하는 프로이다.
엠씨는 {mc}이고, 퀴즈를 맞추면 상금 {reward} 만원을 준다.\
"""

# 2) 여러 값을 리스트 형태로 사용할 경우
# 전개연산자
data = ["강백호", 17, "M", "난 천재니까"]
"""\
이름: {},
나이: {},
성별: {},
좌우명: {}\
""".format(*data)

data = ["강백호", 17, "M", "난 천재니까"]
f"""\
이름: {data[0]},
나이: {data[1]},
성별: {data[2]},
좌우명: {data[3]}\
"""

## 대소문자 변경

# 대문자로 변경
string = "hello"
string.upper()

# 소문자로 변경
string = "HELLO"
string.lower()

## 공백 제거

# 양쪽 = both = left & right = 앞 & 뒤
string = "            안녕              "
string.strip()

# 왼쪽 = left = 앞
string = "            안녕              "
string.lstrip()

# 오른쪽 = right = 뒤
string = "            안녕              "
string.rstrip()

## 문자열 구성 확인

s = "slamdunk01"
s.isalnum()

s.isdigit()

## 문자열 첫번째 위치 반환

# 좌 => 우
# slamdunk01
# 01234
s = "slamdunk01"
s.find("dunk")

# slamdunk01
# 012345678
s.find("0")

# 우 => 좌
# slamslam
# 0123456
s = "slamslam"
s.rfind("a")

# slamslam
# 012
s.find("a")

## in 연산자

print("안녕" in "안녕하세요")

print("잘자" in "안녕하세요")

## split

s = "1 2 3 4 5"
s.split(" ")

cp = "010-1234-5678"
cp.split("-")

# bool

print(True)
print(type(True))

print(False)
print(type(False))

print(1 == 2)
print(1 != 2)
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)

print("가" == "나")
print("가" != "나")
print("가" < "나")
print("가" > "나")

print(True)
print(not True)

x = 5
print(x < 10)
print(not x < 10)

# 조건문

## if 조건문

# 조건문 if문
# 조건이 1개 & 조건 만족할 때 명령어 실행
number = int(input("정수를 입력하세요>"))
if number > 0:
  print("입력한 정수값은 양수입니다.")
if number == 0:
  print("입력한 정수값은 0입니다.")
if number < 0:
  print("입력한 정수값은 음수입니다.")

## 현재 날짜 시간

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.weekday())
# 0: 월, 1: 화, 2: 수, 3: 목, 4: 금, 5: 토, 6: 일

import datetime
now = datetime.datetime.now()
"{}년 {}월 {}일 {}시 {}분 {}초입니다.".format(now.year, now.month, now.day,
                                     now.hour, now.minute, now.second)

# 계절을 알려주는 프로그램
import datetime
now = datetime.datetime.now()
if 3 <= now.month <= 5:
  print("와 봄이야")
if 6 <= now.month <= 8:
  print("야 여름이다")
if 9 <= now.month <= 11:
  print("고독한 가을이야")
if now.month == 12 or 1 <= now.month <= 2:
  print("겨울의 왕국")

print(now)

# 오전 오후를 구별하는 프로그램
import datetime
now = datetime.datetime.now()
korea_hour = now.hour+9
if korea_hour < 12:
  print("현재 오전 {}시입니다. ㅠㅠ".format(korea_hour))
if korea_hour >= 12:
  print("현재 오후 {}시입니다. ^^".format(korea_hour))

# 짝수, 홀수 구분하는 프로그램
no = input("숫자(정수)를 입력하세요> ")
last_no = int(no[-1])
if last_no == 0 or last_no == 2 or last_no == 4 or last_no == 6 or last_no == 8:
  print("현재 입력한 숫자는 짝수입니다.")
if last_no == 1 or last_no == 3 or last_no == 5 or last_no == 7 or last_no == 9:
  print("현재 입력한 숫자는 홀수입니다.")

no = input("숫자(정수)를 입력하세요> ")
last_no = int(no[-1])
if last_no % 2 == 0:
  print("현재 입력한 숫자는 짝수입니다.")
if last_no % 2 == 1:
  print("현재 입력한 숫자는 홀수입니다.")

no = input("숫자(정수)를 입력하세요> ")
last_no = no[-1]
if last_no in "02468":
  print("현재 입력한 숫자는 짝수입니다.")
if last_no in "13579":
  print("현재 입력한 숫자는 홀수입니다.")

## if ~ else 조건문

no = input("숫자(정수)를 입력하세요> ")
last_no = int(no[-1])
if last_no % 2 == 0:
  print("현재 입력한 숫자는 짝수입니다.")
else:
  print("현재 입력한 숫자는 홀수입니다.")

## if ~ elif ~ else 조건문

# 계절을 알려주는 프로그램
import datetime
now = datetime.datetime.now()
if 3 <= now.month <= 5:
  print("와 봄이야")
elif 6 <= now.month <= 8:
  print("야 여름이다")
elif 9 <= now.month <= 11:
  print("고독한 가을이야")
else:
  print("겨울의 왕국")

# 학점을 알려주는 프로그램
# A: 3.5~4.5
# B: 2.5~3.5
# C: 1.5~2.5
# D: 0~1.5
# F: 0
score = float(input("학점을 입력하세요> "))
if 3.5 <= score <= 4.5:
  print("당신의 학점은 A입니다.")
elif 2.5 <= score < 3.5:
  print("당신의 학점은 B입니다.")
elif 1.5 <= score < 2.5:
  print("당신의 학점은 C입니다.")
elif 0 < score < 1.5:
  print("당신의 학점은 D입니다.")
else:
  print("당신의 학점은 F입니다.")

score = float(input("학점을 입력하세요> "))
if 3.5 <= score <= 4.5:
  print("당신의 학점은 A입니다.")
elif 2.5 <= score:
  print("당신의 학점은 B입니다.")
elif 1.5 <= score:
  print("당신의 학점은 C입니다.")
elif 0 < score:
  print("당신의 학점은 D입니다.")
else:
  print("당신의 학점은 F입니다.")

## 조건문에 들어가면 False 로 바뀌는 값

if None:
  print("None 값은 현재 True입니다.")
else:
  print("None 값은 현재 False입니다.")

if 0:
  print("0 값은 현재 True입니다.")
else:
  print("0 값은 현재 False입니다.")

if []:
  print("리스트 값은 현재 True입니다.")
else:
  print("리스트 값은 현재 False입니다.")

if 1:
  print("1 값은 현재 True입니다.")
else:
  print("1 값은 현재 False입니다.")

## pass 키워드

no = input("숫자(정수)를 입력하세요> ")
last_no = int(no[-1])
if last_no % 2 == 0:
  pass
else:
  pass

no = input("숫자(정수)를 입력하세요> ")
last_no = int(no[-1])
if last_no % 2 == 0:
  raise NotImplementedError
else:
  raise NotImplementedError

# 리스트

# 리스트 생성
list_1 = [1,2,3,4,5]
print(list_1)
# 대괄호 안의 개별값 = 요소 = 5개의 요소

list_2 = ["안","녕","하","세","요"]
print(list_2)

list_3 = [1, 2, 3, "안", "녕", True]
print(list_3)

## 인덱싱

list_a = [[1,2,3,4], "안녕하세요", True]
print(list_a)

list_a[0]

list_a[1]

list_a[2]

# 리스트 안의 리스트 접근
list_a[0][2]

list_a[1][2]

## 슬라이싱

# 인덱스 범위
# 끝번호 포함하지 않음
print(list_a[0:2])
print(list_a[0:1+1])

# 시작번호 생략 = 처음부터~
print(list_a[:2])
print(list_a[:1+1])

# 끝번호 생략 = 끝까지~
print(list_a[1:])
print(list_a[1:])

## 음수 인덱스

list_a[-1]

list_a[-2]

list_a[-3]

## 리스트 요소 변경

list_a[2] = False
print(list_a[2])
print(list_a)

list_a[1] = "잘자요"
print(list_a[1])
print(list_a)

list_a[0][0] = 10
print(list_a[0])
print(list_a)

## IndexError

list_a[10]

list_a[3]

list_a[0][4]

#
#
#
# 리스트

## 연결 vs. 추가

# 연결 +
list_1 = [1,2,3]
list_2 = [4,5,6]
print(list_1 + list_2)

# 연결 *
print(list_1 * 3)

# 추가 = 뒤에 추가 = 요소(개별값)
list_1.append(5)
print(list_1) # 파괴적 처리

# 리스트 길이
len(list_1) # 요소의 개수

# 추가 = 중간에 추가 = 원하는 위치(인덱스 번호)에 추가 = 요소(개별값)
list_1.insert(3, 4) # 인덱스 3번 위치에 4라는 값(요소) 추가
print(list_1) # 파괴적 처리

# 추가 = + 연결 & 파괴적 처리 = 리스트 전체 요소
list_1.extend(list_2)
print(list_1) # 파괴적 처리

## 제거

# 인덱스 번호로 제거
# del 키워드 = delete
del list_1[2]
print(list_1)

# pop 함수
list_1.pop(1)
print(list_1)

# 값으로 제거
# remove 함수
list_1.remove(4)
print(list_1)

# 리스트 안의 모든 요소 제거 = 비우기 = 리스트 구조 살아있음
list_1.clear()
print(list_1)

## 정렬

# 오름차순
score = [75,55,40,90,100]
score.sort()
print(score)
# 내림차순
score.sort(reverse=True)
print(score)

# in & not in

print(75 in score)
print(0 in score)
print(75 not in score)
print(0 not in score)

## 전개 연산자

# 1) 리스트 안에서 사용
a = [1,2,3]
b = [*a] # 비파괴적 처리 != append 함수와 다름
c = [*a, *a]
print(a);print(b);print(c)

# 2) 함수에서 사용
print(a)
print(*a)

# 반복문

## 범위

for 반복문 = 반복횟수 지정

# 1) 끝번호, 시작 번호 생략(= 처음부터)
range(10) # 10번 반복
list(range(10))
# range(9+1)

# 2) 시작 번호, 끝번호 & 간격이 1
range(1,10) # 9번 반복
list(range(1,10))
# range(1,9+1)

# 3) 시작 번호, 끝번호, 간격 2
range(1,10, 2) # 5번 반복
list(range(1,10,2))
# range(1,9+1,2)

# for 반복문
for i in range(10):
  print(i) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print("반복") # 10번 반복

for i in range(1,10):
  print(i) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print("반복") # 9번 반복

for i in range(1,10, 2):
  print(i) # [1, 3, 5, 7, 9]
  print("반복") # 5번 반복

## 리스트로 반복문

# 리스트로 반복문
list_a = [1,2,3] # 1차원
list_b = [[1,2,3],[4,5,6]] # 2차원

# 3개의 요소를 가지고 있어서 3번 반복
for i in list_a:
  print(i)

# 2개의 요소를 가지고 있어서 2번 반복
# 여전히 리스트 형태로 출력
for i in list_b:
  print(i)

for i in list_b:
  for j in i:
    print(j)

list_c = [[1,2,3],[4,5,6],7]

for i in list_c:
  print(i)
  for j in i:
    print(j)

for i in list_c:
  if type(i) == list:
    for j in i:
      print(j)
  else:
    print(i)

# 딕셔너리

## 딕셔너리 만들기

# 리스트와 딕셔너리 비교
# 딕셔너리 생성
sd_dic = {
    "이름": "정대만",
    "나이": 19,
    "키": 183,
    "몸무게": 70
}
# 리스트
sd_list = ["정대만",19,183,70]

# 이름 보기
print(sd_list[0])
print(sd_dic["이름"])

# 값
print(sd_list[1])
print(sd_dic["나이"])

print(sd_list[3])
print(sd_dic["몸무게"])

# 값 변경
sd_dic["키"] = 185
print(sd_dic)

# sd_dic{"키"} <= 실수하지 말 것

## 여러 개 값을 가지는 딕셔너리

# 여러 개의 값을 가지는 딕셔너리 생성
bs = {
    "선수": ["채치수","정대만","송태섭","강백호","서태웅"],
    "감독": ["안감독"],
    "매니저": ["한나"]
}
print(bs)

# 값 보기
bs["선수"]

bs["선수"][1]

# 값 변경
bs["매니저"][0] = "소연"
print(bs)

# 새로운 키와 값 추가
# 하나의 값
bs["상대팀"] = "산왕공고"
print(bs)

# 여러 개의 값
bs["별명"] = ["고릴라", "불꽃남자"]
print(bs)

## 키와 값 제거

del bs["상대팀"]
print(bs)

## KeyError

# 존재하지 않는 키를 사용할 때 발생
# 값 보기
bs["상대팀"]

# 키와 값 제거
del bs["상대팀"]

## NameError

# 에러 발생하는 경우
a = {이름: "강백호"}
print(a)

# 에러 수정 = 키가 문자열이면 따옴표로 묶어줘야 함
a = {"이름": "강백호"}
print(a)

## in 연산자

# 찾고 싶은 키
"선수" in bs

"선생님" in bs

# 딕셔너리의 키 존재 여부 알려주는 프로그램
key = input("찾고 싶은 키를 입력하세요> ")
if key in bs:
  print("존재하는 키입니다. 해당 값은 ", bs[key])
else:
  print("존재하지 않는 키입니다.")

## 값을 보여주는 함수

# 존재하는 키로 값 보기
bs["감독"]

# 존재하지 않는 키로 값 보기 = KeyError
bs["감독님"]

# 존재하지 않는 키로 값 보기 = 에러 없이 결과가 없다는 내용
bs.get("감독")

value = bs.get("감독님")
print(value)

# 반복문

## 딕셔너리로 반복문

sd_dic = {
    "이름": "정대만",
    "나이": 19,
    "키": 183,
    "몸무게": 70
}

# 반복문
for i in sd_dic:
  # print(i) # 키
  print(sd_dic[i]) # 값

character = {
    "name": "정대만",
    "number": 14,
    "records": {
        "three_point": 24,
        "rebound": 1
    },
    "schools": ["무석중", "북산고"]
}
for i in character:
  if type(character[i]) == dict:
    for j in character[i]:
      print(character[i][j])
  elif type(character[i]) == list:
    for k in character[i]:
      print(k)
  else:
    print(character[i])

## 범위(계속)

# 매개변수는 정수형이어야 함
n = 20
range(n)

range(n / 2) # float 형이기 때문에 에러 발생

# 몫
range(n // 2)

# 나머지
range(n % 6)

## 리스트와 범위로 반복문

# 인덱스 번호와 값을 동시에 출력
list_a = [21,34,11,5,67]

print(range(len(list_a)))
print(list(range(len(list_a))))

for i in range(len(list_a)):
  print("인덱스", i, "값", list_a[i])

## 역반복문

# 역순으로 반복
# range(0,5+1)
for i in range(5, 1 - 1, -1): # range(5, 0 , -1)
  print(i) # 5번 반복

for i in range(5, 1 - 1, -2): # range(5, 0 , -2)
  print(i) # 3번 반복

for i in reversed(range(1,5+1)):
  print(i)

# 반복문 while

# 무한반복
while True:
  print("언제 끝나")

while True:
  print("언제 끝나", end = "")

## while 문으로 for 문처럼 사용

# 숫자를 0 ~ 9 까지 출력
for i in range(10):
  print(i)

# while 문으로 재현
i = 0
while i < 10:
  print(i)
  i += 1

## 값이 있는 동안에 반복

list_a = [1,2,3,2,4,2,5]
value = 2
while value in list_a:
  list_a.remove(value)

print(list_a)

## 시간 기반으로 반복

import time
number = 0
target = time.time() + 3
while time.time() < target:
  number += 1
print(number)

## break / continue

# 반복 종료
i = 0
while True:
  print(i)
  i += 1
  yn = input("종료할까요? (종료를 원하시면 Y 나 y 를 입력하세요)> ")
  if yn in ["Y", "y"]:
    print("반복 종료")
    break

# 현재 반복 생략하고 다음 반복으로
list_a = [100, 20, 150, 50, 200]
for i in list_a:
  if i < 100:
    continue
  print(i)

# 문자열, 리스트, 딕셔너리와 관련된 함수

list_a = [1,2,3,4,5]
print(min(list_a))
print(max(list_a))
print(sum(list_a))

print(min(1,2,3,4,5))
print(max(1,2,3,4,5))

# 역순
list_a = [1,2,3,4,5]
list_b = reversed(list_a)
print(list_a)
print(list_b) # 이터레이터 객체
print(list(list_b))
# 역반복문
for i in reversed(list_a):
  print(i)

# 인덱스와 값을 동시에 출력 => 함수로 해결
list_a = [21,34,11,5,67]

# 1) 리스트
i = 0
for j in list_a:
  print("인덱스", i, "값", j)
  i += 1

# 2) 리스트 & 범위
for i in range(len(list_a)):
  print("인덱스", i, "값", list_a[i])

# 3) enumerate 함수 with 리스트
list(enumerate(list_a)) # 튜플 형태로 반환

for i, j in enumerate(list_a):
  print("인덱스", i, "값", j)

# 4) items 함수 with 딕셔너리
# 키와 값을 동시에 출력
sd_dic = {
    "이름": "정대만",
    "나이": 19,
    "키": 183,
    "몸무게": 70
}
sd_dic.items()

for i, j in sd_dic.items():
  print("키", i, "값", j)

## 리스트 내포

list_a = []
list_b = []
for i in range(1,5+1):
  list_a.append(i)
  list_b.append(i ** 2)

print(list_a);print(list_b)

# 리스트 내포로 재현
list_c = [i ** 2 for i in range(1,5+1)]
print(list_c)

# 리스트 내포에 조건문 추가
# 과일만 리스트로 저장
list_a = ["사과", "참외", "수박", "토마토"]
fruit = [i # 표현식(값 표현)
         for i in list_a # 반복문
         if i != "토마토"] # 조건문
print(fruit)




#
#
# /




# 문자열, 리스트, 딕셔너리와 관련된 함수(계속)

## 여러 줄의 문자열 출력

# 홀수, 짝수 구분하는 프로그램
number = int(input("정수를 입력하세요> "))
if number % 2 == 0: # 짝수
  print("""\
  입력한 숫자는 {}입니다.
  {}는 짝수입니다.\
  """.format(number, number))
else: # 홀수
  print("""\
  입력한 숫자는 {}입니다.
  {}는 홀수입니다.\
  """.format(number, number))

# 들여쓰기가 되는 문제를 해결해보자
number = int(input("정수를 입력하세요> "))
if number % 2 == 0: # 짝수
  print("""\
입력한 숫자는 {}입니다.
{}는 짝수입니다.\
  """.format(number, number))
else: # 홀수
  print("""\
입력한 숫자는 {}입니다.
{}는 홀수입니다.\
  """.format(number, number))
# 코드의 일관성이 없음 = 가독성이 떨어짐

number = int(input("정수를 입력하세요> "))
if number % 2 == 0: # 짝수
  print("입력한 숫자는 {}입니다.\n{}는 짝수입니다.".format(number, number))
else: # 홀수
  print("입력한 숫자는 {}입니다.\n{}는 홀수입니다.".format(number, number))

## 문자열 연결

print("-".join(["010", "1234", "5678"]))
print(" ".join(["010", "1234", "5678"]))
print("|".join(["010", "1234", "5678"]))

number = int(input("정수를 입력하세요> "))
if number % 2 == 0: # 짝수
  print("\n".join(["입력한 숫자는 {}입니다.", "{}는 짝수입니다."]).format(number, number))
else: # 홀수
  print("\n".join(["입력한 숫자는 {}입니다.", "{}는 홀수입니다."]).format(number, number))

# 소괄호로 문자 연결 => , 없이 사용해야 함!
a = (
    "나는 "
    "여름을 "
    "좋아합니다"
)
print(a)
print(type(a))

a = (
    "나는 ",
    "여름을 ",
    "좋아합니다"
)
print(a)
print(type(a))

a = (
    "나는 \n"
    "여름을 \n"
    "좋아합니다"
)
print(a)
print(type(a))

number = int(input("정수를 입력하세요> "))
if number % 2 == 0: # 짝수
  print(("입력한 숫자는 {}입니다.\n"
         "{}는 짝수입니다.").format(number, number))
else: # 홀수
  print(("입력한 숫자는 {}입니다.\n"
         "{}는 홀수입니다.").format(number, number))

## 이터레이터

a = [1,2,3]
b = reversed(a)
print(b) # iterator object
print(list(b))
print(list(b)) # 메모리 효율성

a = [1,2,3]
b = list(reversed(a))
print(b);print(b)

a = [1,2,3]
b = reversed(a)
print(next(b))
print(next(b))
print(next(b))

# 함수

## 사용자 정의 함수

def print3times():
  print("안녕")
  print("안녕")
  print("안녕")

print3times()

## 일반매개변수

# 일반매개변수 = 값을 순서대로 입력
def printntimes(value, n):
  for i in range(n): # n 은 반드시 정수
    print(value) # 무슨 값이든 상관 없음

printntimes("안녕", 3)

printntimes("안녕", 3/2) # range 에 정수형이 들어 가야하기 때문에 에러 발생

printntimes()

printntimes("안녕")

printntimes(3,3)

printntimes(3,3,3)

## 가변매개변수

# 가변매개변수 = 입력할 수 있는 값의 개수 제한이 없음
# 일반매개변수 뒤에 와야 함
def printntimes(n, *values):
  for i in range(n): # n 은 반드시 정수
    for j in values:
      print(j)

printntimes(3, "안녕", "파이썬", "재밌니")

## 기본매개변수

# 기본매개변수 = 기본값을 가지는 매개변수
# 가변매개변수 뒤에 기본매개변수
def printntimes(*values, n = 3):
  for i in range(n): # n 은 반드시 정수
    for j in values:
      print(j)

printntimes("안녕", "파이썬", "재밌니")
# 일반매개변수 - 가변매개변수 - 기본매개변수

## 키워드 매개변수

# 매개변수의 이름을 지정해서 입력
# 가변매개변수 뒤에서 사용
printntimes("안녕", "파이썬", "재밌니", n = 5)

printntimes("안녕", "파이썬", "재밌니", 5)

printntimes(n = 5, "안녕", "파이썬", "재밌니")

# 키워드 매개변수를 사용하면 좋은 점
# 순서 고려하지 않아도 됨
def test(a, b = 3, c = 4):
  print(a + b + c)

# 1) 기본 형태로 사용 = 매개변수 순서대로 입력
test(2,4,6)

test(2)

# 2) 키워드 매개변수로 입력
test(a = 2)

test(a = 2, b = 4, c = 7)

# 3) 키워드 매개변수 순서를 바꿔 입력
test(c = 7, b = 4, a = 2)

# 4) 키워드 매개변수 일부만 사용
test(a = 2, c = 7)

test(2, c = 7)

## 리턴

# 리턴 = 반환값, 리턴값 = 함수 적용 결과
# 1) 자료 없이 리턴
def return_test():
  print("A")
  return # 여기까지 실행
  print("B")
return_test()

# 2) 자료와 함께 리턴
def return_test():
  return "B"
return_test()

# 가장 일반적인 방식
def return_test():
  a = 3 + 2
  return a
return_test()

# 3) None 리턴
def return_test():
  return
a = return_test()
print(a)

## 입력한 값을 모두 더하는 함수

# 일반매개변수
def sum_all(start, end):
  output = 0
  for i in range(start, end+1):
    output += i
  return output

# 일반매개변수로 사용 = 순서대로 입력
sum_all(1,3)

# 키워드 매개변수로 사용 = 순서 상관 없음
sum_all(start = 1, end = 3)

sum_all(end = 3, start = 1)

# 기본매개변수
# 간격을 추가해서 합계
def sum_all(start = 1, end = 10, step = 2):
  output = 0
  for i in range(start, end+1, step):
    output += i
  return output

sum_all()

# 일반매개변수로 사용 = 순서대로 입력
sum_all(1, 5, 2)

# 키워드 매개변수로 사용 = 순서 상관 없음
sum_all(start = 1, end = 5, step = 2)

sum_all(step = 2, start = 1, end = 5, )

# 키워드 매개변수 일부만 사용
sum_all(start = 1, step = 2)

# 함수의 활용

## 재귀함수

# 팩토리얼
# 반복문으로 구현
def factorial(n):
  output = 1
  for i in range(1,n+1):
    output *= i
  return output

print(factorial(1))
print(factorial(2))
print(factorial(3))

def factorial(n):
  output = 1
  for i in range(n,1-1,-1):
    output *= i
  return output

print(factorial(1))
print(factorial(2))
print(factorial(3))

# 재귀함수로 구현
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
    # n = 3
    # 3 * factorial(2)
    # 3 * 2 * factorial(1)
    # 3 * 2 * 1 * factorial(0)
    # 3 * 2 * 1 * 1 = 6

print(factorial(1))
print(factorial(2))
print(factorial(3))

## 피보나치 수열

# 피보나치 수열 = 앞의 두 숫자를 합한게 다음 숫자
def fibonacci(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
    # n = 3
    # f(3) = f(2) + f(1) = 1 + 1 = 2
    # n = 4
    # f(4) = f(3) + f(2) = f(2) + f(1) + 1 = 2 + 1 = 3

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

print(fibonacci(25))

print(fibonacci(50)) # 같은 계산 반복하는 문제 발생

## 키워드 global

# 재귀 함수 사용 횟수 계산
# 함수 밖에 있는 변수 참조하기 위해서 global 키워드가 필요
count = 0
def fibonacci(n):
  global count
  count += 1
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(1))
print(count)

count = 0
def fibonacci(n):
  global count
  count += 1
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(2))
print(count)

count = 0
def fibonacci(n):
  global count
  count += 1
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(25))
print(count)

# global 키워드가 없는 경우
count = 0
def fibonacci(n):
  count # 여기에 global 키워드 넣어야 에러 없음
  count += 1
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(25))
print(count)

## 메모화

f_dict = {
    1: 1,
    2: 1
}
# 조기리턴
def fibonacci(n): # n 은 딕셔너리 키
  if n in f_dict:
    return f_dict[n] # 존재하는 키의 값을 가져오는 경우 = 계산한 것이 있음
  output = fibonacci(n-1) + fibonacci(n-2)
  f_dict[n] = output # 존재하지 않는 키의 값을 저장하는 경우 = 계산한 것이 없음
  return output

print(fibonacci(50))

f_dict

# 조기리턴 사용하지 않는 경우
def fibonacci(n): # n 은 딕셔너리 키
  if n in f_dict:
    return f_dict[n] # 존재하는 키의 값을 가져오는 경우 = 계산한 것이 있음
  else:
    output = fibonacci(n-1) + fibonacci(n-2)
    f_dict[n] = output # 존재하지 않는 키의 값을 저장하는 경우 = 계산한 것이 없음
    return output

## 리스트 평탄화

# 2차원 리스트 반복문 2번 사용해서 평탄화
# 실제로 중괄호가 몇 번 나올지 예상할 수 없음
# 재귀함수로 해결 가능
def flat(data):
  output = []
  for i in data: # 반복
    if type(i) == list: # 리스트인 경우
      output += flat(i) # 리스트가 아닐 때까지 반복
    else: # 요소인 경우
      output.append(i) # 요소 추가
  return output
# [1,2,3] => flat([1,2,3]) => 리스트 아니므로 요소 추가
# [4, [5, 6]] => flat([4, [5, 6]]) => 4는 요소 추가
# [5, 6] => flat([5, 6]) => 리스트 아니므로 요소 추가
# 7 => 리스트 아니므로 요소 추가
# [8,9] => flat([8,9]) => 리스트 아니므로 요소 추가

a = [[1,2,3], [4, [5, 6]], 7, [8,9]]
print(a)
print(flat(a))

def flat(data):
  output = []
  for i in data: # 반복
    if type(i) == list: # 리스트인 경우
      output += flat(i) # 리스트가 아닐 때까지 반복
    else: # 요소인 경우
      output += i # 요소 추가가 아닌 리스트 연결
      output.extend(i) # 요소 추가가 아닌 리스트 연결
  return output
a = [[1,2,3], [4, [5, 6]], 7, [8,9]]
print(a)
print(flat(a))

# 튜플

# 튜플 생성
list_a = [1,2,3]
tuple_a = (1,2,3)
print(list_a); print(tuple_a)
print(type(list_a)); print(type(tuple_a))

print(list_a[0]);print(list_a[1]);print(list_a[2])
print(tuple_a[0]);print(tuple_a[1]);print(tuple_a[2])

list_a[0] = 10
print(list_a)

tuple_a[0] = 10
print(tuple_a) # 튜플은 요소 변경 불가

# 소괄호 없이 튜플 생성
tuple_a = 1,2,3
print(tuple_a)
print(type(tuple_a))

# 여러 변수를 한 번에 할당
[a, b] = [1, 2]
(c, d) = (3, 4)
print(a);print(b);print(c);print(d)
print(type(a));print(type(b));print(type(c));print(type(d))

# 이렇게 하지 말고 위의 방법 참고
a = 1
b = 2
c = 3
d = 4

# 소괄호 없이 여러 변수에 값 할당
a, b, c = 1, 2, 3
print(a);print(b);print(c)
print(type(a));print(type(b));print(type(c))

## 값의 교환

a = 1
b = 2
print(a);print(b)
c = a
a = b
b = c
print(a);print(b)

a, b = 1, 2
print(a);print(b)
a, b = b, a
print(a);print(b)

## 튜플 & 함수

# 튜플 형태로 리턴하는 사용자 정의 함수 만들기
def test():
  return (1, 2)
a, b = test()
# a, b = (1, 2)
print(a);print(b)

# 튜플 형태로 리턴하는 함수 복습
# 리스트의 인덱스와 값 반환 = enumerate()
for i, j in enumerate([1,2,3]):
  print("인덱스", i, "값", j)

# 딕셔너리의 키와 값 반환 = items()
for i, j in {0:1, 1:2, 2:3}.items():
  print("키", i, "값", j)

# 몫 & 나머지
a, b = 63, 30
print(a // b) # 몫
print(a % b) # 나머지

# 몫과 나머지 값을 튜플 형태로 반환하는 함수
c, d = divmod(a, b)
print(c);print(d)

# 람다

# 함수의 매개변수에 사용하는 함수 = 콜백 함수
def repeat_10(x):
  for i in range(10):
    x() # 함수 사용 = print_hi()
def print_hi():
  print("hi")
repeat_10(print_hi) # print_hi = 콜백 함수

# map 함수 = 콜백 함수 적용 결과 값
def sqr(x):
  return x ** 2
list_a = [1,2,3]
output_map = map(sqr, list_a)
print(output_map)
print(list(output_map))

# filter 함수 = 콜백 함수 적용 결과 중에서 True 인 것
def under_3(x):
  return x < 3
list_a = [1,2,3]
output_filter = filter(under_3, list_a)
print(output_filter)
print(list(output_filter))

# 람다로 변경
list_a = [1,2,3]
# 콜백 함수 자리에 람다
# 람다 사용법: lambda 매개변수: 리턴값(기능 결과)
output_map = map(lambda x: x ** 2, list_a)
print(output_map)
print(list(output_map))

list_a = [1,2,3]
output_filter = filter(lambda x: x < 3, list_a)
print(output_filter)
print(list(output_filter))




#
#
#




# 리스트에서 사용했던 함수를 딕셔너리에서 사용하는 방법

## 최소값, 최대값

# 딕셔너리 형태의 요소를 가지고 있는 리스트
players = [{"이름": "강백호",
            "신장": 189},
           {"이름": "서태웅",
            "신장": 188},
           {"이름": "채치수",
            "신장":195}]
def height(players):
  return players["신장"]
print(min(players, key = height)) # 최소값
print(max(players, key = height)) # 최대값

# 리스트
player_list = [189,188,195]
print(min(player_list)) # 최소값
print(max(player_list)) # 최대값

players = [{"이름": "강백호",
            "신장": 189},
           {"이름": "서태웅",
            "신장": 188},
           {"이름": "채치수",
            "신장":195}]
def height(i): # i 가 딕셔너리 players
  return i["신장"] # = players["신장"]
# min, max 함수 안에서
# key 에서 사용하고 있는 함수의 매개변수로 딕셔너리 players 사용
print(min(players, key = height)) # 최소값
print(max(players, key = height)) # 최대값

# 람다로 변경
players = [{"이름": "강백호",
            "신장": 189},
           {"이름": "서태웅",
            "신장": 188},
           {"이름": "채치수",
            "신장":195}]
print(min(players, key = lambda x: x["신장"])) # 최소값
print(max(players, key = lambda x: x["신장"])) # 최대값

# 매개변수 이름만 변경되었을 뿐, 위의 결과와 동일함
print(min(players, key = lambda player: player["신장"])) # 최소값
print(max(players, key = lambda player: player["신장"])) # 최대값

## 정렬

# 리스트 정렬
# 오름차순
a = [1,45,72,23,8]
a.sort()
print(a)

# 내림차순
a = [1,45,72,23,8]
a.sort(reverse=True)
print(a)

# 오름차순
players = [{"이름": "강백호",
            "신장": 189},
           {"이름": "서태웅",
            "신장": 188},
           {"이름": "채치수",
            "신장":195}]
players.sort(key = lambda x: x["신장"])
print(players)

# 내림차순
players = [{"이름": "강백호",
            "신장": 189},
           {"이름": "서태웅",
            "신장": 188},
           {"이름": "채치수",
            "신장":195}]
players.sort(key = lambda x: x["신장"], reverse=True)
print(players)

# 텍스트 파일 처리

## 파일 열기 & 닫기

# 파일 열기
file = open('base.txt', "w")
# 텍스트 쓰기
file.write("안녕 파이썬 재밌니")
# 파일 닫기
file.close()

# 파일을 열고 닫는 과정에 코드가 많이 생기면 파일 닫지 않는 실수를 함
# 이를 방지하기 위해서 with 문
with open('base.txt', "w") as file:
  # 텍스트 쓰기
  file.write("안녕 파이썬 재밌니")
# with 문이 끝나면 자동으로 파일이 닫힘

## 텍스트 파일 한줄씩 읽기

# 이름, 키, 몸무게 => csv 텍스트 파일로 저장
import random
hangul = list("가나다라마바사아자차타파하")
with open('info.txt', "w") as file:
  for i in range(1000):
    name = random.choice(hangul)+random.choice(hangul)+random.choice(hangul)
    height = random.randrange(140,200)
    weight = random.randrange(40,150)
    file.write("{}, {}, {}\n".format(name,height,weight))

# 텍스트 파일 한줄씩 읽기 & 새로운 변수 생성 및 출력
with open('info.txt', "r") as file:
  for line in file:
    name, height, weight = line.strip().split(", ")
    if (not name) or (not height) or (not weight):
      continue
    # 체중(kg)/키(m)제곱
    bmi = int(weight) / (int(height)/100)**2
    result = ""
    # 25 보다 크거나 같으면 과체중
    # 18.5 보다 크거나 같으면 정상
    # 나머지 저체중
    if bmi >= 25:
      result = "과체중"
    elif bmi >= 18.5:
      result = "정상"
    else:
      result = "저체중"
    # print("이름: {}, 키: {}, 몸무게: {}, BMI: {}, 결과: {}".format(name,height,weight,bmi,result))
    print("\n".join(["이름: {}",
                     "키: {}",
                     "몸무게: {}",
                     "BMI: {}",
                     "결과: {}"]).format(name,height,weight,bmi,result))

# 예외 처리

## 구문 오류

# 오타가 일반적 = SyntaxError
# 프로그램 실행 전에 발생하는 오류
print("안녕 점심시간 기다려지니)

## 예외

# = 런타임오류
# 프로그램 실행 중에 발생하는 오류
list_z[0]

# 예외 수정
list_z = [1,2]
list_z[0]

## 예외 상황 만들기

# 원의 반지름을 입력해서 원의 둘레와 넓이 계산해주는 프로그램
# 실수나 문자를 포함한 숫자를 입력해서 예외 상황 만들기
number = int(input("원의 반지름을 입력하세요(단, 정수)>"))
pi = 3.14
print("원의 반지름", number)
print("원의 둘레", 2*pi*number)
print("원의 넓이", pi*number*number)

# 조건문으로 예외 처리
number = input("원의 반지름을 입력하세요(단, 정수)>")
pi = 3.14
if number.isdigit(): # 문자열이 숫자로 변환할 수 있는 경우
  number = int(number)
  print("원의 반지름", number)
  print("원의 둘레", 2*pi*number)
  print("원의 넓이", pi*number*number)
else:
  print("정수를 입력해주시겠어요?")

## try ~ except

# try ~ except 구문
try:
  number = input("원의 반지름을 입력하세요(단, 정수)>")
  pi = 3.14
  number = int(number)
  print("원의 반지름", number)
  print("원의 둘레", 2*pi*number)
  print("원의 넓이", pi*number*number)
except:
  print("정수를 입력해주시겠어요?")

# pass 사용 가능
try:
  number = input("원의 반지름을 입력하세요(단, 정수)>")
  pi = 3.14
  number = int(number)
  print("원의 반지름", number)
  print("원의 둘레", 2*pi*number)
  print("원의 넓이", pi*number*number)
except:
  pass

# 예외 강제 발생
try:
  number = input("원의 반지름을 입력하세요(단, 정수)>")
  pi = 3.14
  number = int(number)
  print("원의 반지름", number)
  print("원의 둘레", 2*pi*number)
  print("원의 넓이", pi*number*number)
except:
  raise NotImplementedError

## try ~ except ~ else

# try ~ except ~ else 구문
try: # 예외 발생할 수 있는 코드 입력
  number = input("원의 반지름을 입력하세요(단, 정수)>")
  pi = 3.14
  number = int(number)
except: # 예외 발생할 때 처리할 코드
  print("정수를 입력해주시겠어요?")
else: # 예외 발생하지 않을 때 처리할 코드
  print("원의 반지름", number)
  print("원의 둘레", 2*pi*number)
  print("원의 넓이", pi*number*number)

## try ~ except ~ else ~ finally

# try ~ except ~ else ~ finally 구문
try: # 예외 발생할 수 있는 코드 입력
  number = input("원의 반지름을 입력하세요(단, 정수)>")
  pi = 3.14
  number = int(number)
except: # 예외 발생할 때 처리할 코드
  print("정수를 입력해주시겠어요?")
else: # 예외 발생하지 않을 때 처리할 코드
  print("원의 반지름", number)
  print("원의 둘레", 2*pi*number)
  print("원의 넓이", pi*number*number)
finally:
  print("하여튼 프로그램이 정상적으로 종료되었어요")

# 예외객체

# 예외 정보를 저장하는 객체
try:
  number = input("원의 반지름을 입력하세요(단, 정수)>")
  pi = 3.14
  number = int(number)
  print("원의 반지름", number)
  print("원의 둘레", 2*pi*number)
  print("원의 넓이", pi*number*number)
except Exception as exception: # 예외객체
  print("예외 종류: ", type(exception))
  print("예외 객체: ", exception)

# 여러가지 예외 상황 (2가지)
a = [1,2,3,4,5] # 0 ~ 4
try:
  # 1 번째 예외 상황: 정수가 아닌 문자열 입력 (4번째라고 입력)
  number = int(input("정수를 입력하세요> "))
  # 2 번째 예외 상황: 인덱스에 없는 정수 번호를 입력한 경우 (10 입력)
  print("{} 번째 요소는 {}입니다.".format(number, a[number]))
except Exception as exception: # 예외객체
  print("예외 종류: ", type(exception))
  print("예외 객체: ", exception)

## 예외구분

a = [1,2,3,4,5] # 0 ~ 4
try:
  # 1 번째 예외 상황: 정수가 아닌 문자열 입력 (4번째라고 입력)
  number = int(input("정수를 입력하세요> "))
  # 2 번째 예외 상황: 인덱스에 없는 정수 번호를 입력한 경우 (10 입력)
  print("{} 번째 요소는 {}입니다.".format(number, a[number]))
except ValueError:
  print("정수를 입력주시겠어요?")
except IndexError:
  print("정수를 잘 입력하셨지만 인덱스 범위에 있는 정수를 입력해주세요")
# try 구문에서 코드를 계속 입력한다고 가정
# 어떤 예외가 발생할지 모름 = 대처가 안됨

# 3번째 예외상황 만들기
a = [1,2,3,4,5] # 0 ~ 4
try:
  # 1 번째 예외 상황: 정수가 아닌 문자열 입력 (4번째라고 입력)
  number = int(input("정수를 입력하세요> "))
  # 2 번째 예외 상황: 인덱스에 없는 정수 번호를 입력한 경우 (10 입력)
  print("{} 번째 요소는 {}입니다.".format(number, a[number]))
  # 3 번째 예외 상황: 식별자에 없는 이름 사용 (3 입력)
  예외발생해라()
except ValueError:
  print("정수를 입력주시겠어요?")
except IndexError:
  print("정수를 잘 입력하셨지만 인덱스 범위에 있는 정수를 입력해주세요")
# try 구문에서 코드를 계속 입력한다고 가정
# 어떤 예외가 발생할지 모름 = 대처가 안됨

# 예상할 수 없는 예외도 대처
a = [1,2,3,4,5] # 0 ~ 4
try:
  # 1 번째 예외 상황: 정수가 아닌 문자열 입력 (4번째라고 입력)
  number = int(input("정수를 입력하세요> "))
  # 2 번째 예외 상황: 인덱스에 없는 정수 번호를 입력한 경우 (10 입력)
  print("{} 번째 요소는 {}입니다.".format(number, a[number]))
  # 3 번째 예외 상황: 식별자에 없는 이름 사용 (3 입력)
  예외발생해라()
except ValueError as exception:
  print("정수를 입력주시겠어요?")
  print("예외 객체: ", exception)
except IndexError as exception:
  print("정수를 잘 입력하셨지만 인덱스 범위에 있는 정수를 입력해주세요")
  print("예외 객체: ", exception)
except Exception as exception:
  print("예외 종류: ", type(exception))
  print("예외 객체: ", exception)

# 모듈

## 표준모듈

# = 내장 모듈
import math

math.sin(1)

math.cos(1)

math.tan(1)

math.floor(3.14)

math.ceil(3.14)

import math as m
m.sin(1)

from math import sin, cos, tan
sin(1)

import random

random.random() # 실수

random.uniform(10,20) # 범위에 있는 실수

random.randrange(130,210) # 범위에 있는 정수

random.randrange(10) # 범위에 있는 정수

random.choice([1,2,3,4,5])

a = [1,2,3,4,5]
random.shuffle(a)
print(a)

random.sample(a, k = 2)

import sys

sys.argv

sys.copyright

sys.version

import os

os.name

os.getcwd()

os.listdir()

os.mkdir("hello")

os.rmdir("hello")

with open("test.txt", "w") as file:
 file.write("이제 파이썬 끝나간다")
 os.rename("test.txt", "new.txt")

os.remove("new.txt")

import datetime

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

import time

print("지금부터 3초동안 꼼짝마")
time.sleep(3)
print("얼음 땡")

from urllib import request

url_target = request.urlopen("https://www.google.com/")
output = url_target.read()
print(output)

# 클래스

# 객체 생성
players = [
    {"name": "정대만", "point3": 24, "point2": 6, "rebound": 1},
    {"name": "강백호", "point3": 0, "point2": 4, "rebound": 10},
    {"name": "서태웅", "point3": 12, "point2": 16, "rebound": 5}
]
for player in players:
  score_sum = player["point3"] + player["point2"]
  print(player["name"], score_sum)

# 함수로 객체 만들기
def create_player(name, point3, point2, rebound):
  return {"name": name,
          "point3": point3,
          "point2": point2,
          "rebound": rebound}
players = [
    create_player("정대만", 24, 6, 1),
    create_player("강백호", 0, 4, 10),
    create_player("서태웅", 12, 16, 5)
]
for player in players:
  score_sum = player["point3"] + player["point2"]
  print(player["name"], score_sum)

def create_player(name, point3, point2, rebound):
  return {"name": name,
          "point3": point3,
          "point2": point2,
          "rebound": rebound}
def score_sum(player):
  return player["point3"] + player["point2"]
players = [
    create_player("정대만", 24, 6, 1),
    create_player("강백호", 0, 4, 10),
    create_player("서태웅", 12, 16, 5)
]
for player in players:
  print(player["name"], score_sum(player))

# 클래스
class Player:
  def __init__(self, name, point3, point2, rebound):
    self.name = name
    self.point3 = point3
    self.point2 = point2
    self.rebound = rebound
players = [
    Player("정대만", 24, 6, 1),
    Player("강백호", 0, 4, 10),
    Player("서태웅", 12, 16, 5)
]
print(players[0].name)
print(players[0].point3)
print(players[0].point2)
print(players[0].ft)

# 클래스 안의 함수 = 메소드, 메서드
class Player:
  def __init__(self, name, point3, point2, rebound):
    self.name = name
    self.point3 = point3
    self.point2 = point2
    self.rebound = rebound
  def score_sum(self):
    return self.point3 + self.point2
players = [
    Player("정대만", 24, 6, 1),
    Player("강백호", 0, 4, 10),
    Player("서태웅", 12, 16, 5)
]
for player in players:
  print(player.name, player.score_sum())

