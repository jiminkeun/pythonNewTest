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