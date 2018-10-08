a='python'
b=123
c= ['a','b']
d={'name':'jiminkeun'}

e,f = 'abc', 'bcd'

print(e)
print(f)

k='Hello' + " World"
print(k.split())

l='Hello^World^!!^Name'
print(l.split('^'))
print(l.find('World'))


tuples = (1,100, '수학', 100)

print(tuples[0])
print(tuples[2])

print(tuples.count(100))

tuple1 = (1,2,3,'a','b', 'c')
print(tuple1[:2])

print(tuples+tuple1)
print(tuple1*3)


dictionary = {
    'Name' : '홍길동',
    'Email' : 'gdHone@naver.com',
    '주소' : '서울시 광진구'
}

print(type(dictionary))
print(dictionary.keys())
print(dictionary.values())

for item in dictionary.items():
    print(item)

set1 = set(['서울','대구','대전','부산','인천','강원'])
set2 = set(['서울','부산','강원','충청','광주'])

print(set1.union(set2))         # 합집합
print(set1.intersection(set2))  # 교집합
print(set1.difference(set2))    # 차집합
print(set1.symmetric_difference(set2))  # 둘 중 하나에만 속하는 값(합집합-교집합)