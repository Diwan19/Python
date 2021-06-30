x = range(6)
print(x)
print(type(x))

diction1 = {"name": "himanshu", "age":24, "height":5.9}
for i in diction1:
    print(i)

set1={"tatapower","jswenergy","rpower"}
print(set1)
set1.add("veerenergy")
print(set1)
set1.discard("veerenergy")
set1.add("M&M")

set2=set1
print(set2)

a= frozenset({"apple","kiwi","pineapple"})
print(a)
