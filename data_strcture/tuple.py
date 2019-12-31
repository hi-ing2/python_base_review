# tuple == tuple() == ()

x = (1,3,2,4)
y = ("hello", "world")
z = ("hello", 1,3,2)

x[0] = 10 #튜플은 수정불가능 (불변) 
print(x[1:2]) #이상~미만
print(len(y))
print(sorted(x)) #오름차순 정렬
print(sum(x))
print(sorted(x))

for n in x: #0번째 요소부터 n에 하나씩 넣어라
    print(n)

print(y.index("hello"))  #0번째
#print(y.index("nice"))  #없다고 오류뜸
print("hello" in y)