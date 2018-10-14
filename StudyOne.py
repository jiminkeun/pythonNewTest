a='python'
b=123
c= ['a','b']
d={'name':'jiminkeun'}

e,f = 'abc', 'bcd'

print(e)
print(f)
#abc
#bcd

k='Hello' + " World"
print(k.split())
#['Hello', 'World']

l='Hello^World^!!^Name'
print(l.split('^'))
print(l.find('World'))
#['Hello', 'World', '!!', 'Name']
#6

tuples = (1,100, '수학', 100)

print(tuples[0])
print(tuples[2])
print(tuples.count(100))
#1
#수학
#2

tuple1 = (1,2,3,'a','b', 'c')
print(tuple1[:2])
print(tuples+tuple1)
print(tuple1*3)
#(1, 2)
#(1, 100, '수학', 100, 1, 2, 3, 'a', 'b', 'c')
#(1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c')

dictionary = {
    'Name' : '홍길동',
    'Email' : 'gdHone@naver.com',
    '주소' : '서울시 광진구'
}

print(type(dictionary))
print(dictionary.keys())
print(dictionary.values())
#<class 'dict'>
#dict_keys(['Name', 'Email', '주소'])
#dict_values(['홍길동', 'gdHone@naver.com', '서울시 광진구'])

for item in dictionary.items():
    print(item)
#('Name', '홍길동')
#('Email', 'gdHone@naver.com')
#('주소', '서울시 광진구')

for k,v in dictionary.items():
    print("%s -> %s" % (k, v))
#Name -> 홍길동
#Email -> gdHone@naver.com
#주소 -> 서울시 광진구

for k in dictionary.keys():
    print("%s => %s" % (k, dictionary[k]))
#Name => 홍길동
#Email => gdHone@naver.com
#주소 => 서울시 광진구


price = 10000
day = 1
while day<6:
    price = price + (price*0.3)
    print(round(price))
    day = day+1

#13000
#16900
#21970
#28561
#37129

set1 = set(['서울','대구','대전','부산','인천','강원'])
set2 = set(['서울','부산','강원','충청','광주'])

print(set1.union(set2))         # 합집합
print(set1.intersection(set2))  # 교집합
print(set1.difference(set2))    # 차집합
print(set1.symmetric_difference(set2))  # 둘 중 하나에만 속하는 값(합집합-교집합)
#{'대구', '서울', '부산', '인천', '강원', '대전', '충청', '광주'}
#{'부산', '서울', '강원'}
#{'대구', '대전', '인천'}
#{'인천', '대구', '대전', '충청', '광주'}


for i in range(0,5):
    print("*", end='')

#*****
print("")

for i in range(0,5):
    for j in range(0,5):
        print("*", end='')
    print("")

'''
*****
*****
*****
*****
*****
'''

for i in range(0,5):
    for j in range(0,i+1):
        print("*", end='')
    print('')
'''
*
**
***
****
*****
'''

for i in range(0,5):
    for j in range(0,5-i):
        print("*", end='')
    print('')
'''   
*****
****
***
**
*
'''

for i in range(0,5):
    for j in range(0,5):
        if(4-i < j+1):
            print("*", end='')
        else:
            print(" ", end='')
    print('')

'''
    *
   **
  ***
 ****
*****
'''

for i in range(0,5):
    for j in range(0,5):
        if i < j+1:
            print("*", end='')
        else:
            print(" ", end='')
    print('')

'''
*****
 ****
  ***
   **
    *
'''

for i in range(0,5):
    for k in range(0,(4 - i)):
        print(' ', end='')
    for j in range(0,i+(i+1)):
        print("*", end='')

    print('')

'''
    *
   ***
  *****
 *******
*********
'''


for i in range(0,5):
    for k in range(0,i):
        print(' ', end='')
    for j in range(0,10-(i+(i+1))):
        print("*", end='')

    print('')

'''
*********
 *******
  *****
   ***
    *
'''

apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for store in apart:
    for home in store:
        if home in arrears:
            continue
        else:
            print("배달완료 : ", home)
