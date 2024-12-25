dic = {"22CT01" : 1, "22CT02" : 2,"22CT03" : 3,"22CT04":4}
print(dic)
print(dic.keys())
print(dic.values())
dic["22CT05"] = 5 #add
dic["22CT02"] = 10 #update
dic.pop("22CT01") # remove
for x, y in dic.items():
    print(x,y)
