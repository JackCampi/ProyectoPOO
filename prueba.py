print("hello world")
a = 54
if a < 49:
    print("hello")
else:
    print("no hello")
b = 54 +65j
print(b)
mainList=[{"name":"tu","album":"donde estan los ladrones"},{"name": "nothing on you", "album":"no. 6"}, {"name": "demons", "album":"night visions"}]
print(mainList)
print("--------------------------------------")
key = "name"
elements = []
for i in range(len(mainList)):
  elements.append(mainList[i][key])

print(elements)
print("--------------------------------------")
elements.sort()
print(elements)
print("--------------------------------------")
result = []
for i in range(len(elements)):
  for j in range(len(mainList)):
    if elements[i] == mainList[j][key]:
      result.append(mainList[j])

print(result)
