results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]
#list of dictionary
#win % tvm
#list comprehension
results.sort(key=lambda re:re['win'],reverse=True)
print(results)
print(max(results,key=lambda f:f['win']))
print(min(results,key=lambda f:f["win"]))
aplus=sum([res['A+']for res in results])
print(aplus)
#total win percentage
winper=(res['A+'],for res in results)
print(winper)

