#set operations
#1.union operations

#2.intersection operations

#3.difference

#union operations
#...........................
#combine of two sets     duplicate values does not repeat

st={10,20,30,40,60,}
st1={11,20,21,31,41,61}

u=st.union(st1)
print(u)

#intersection
st3=st.intersection(st1)
print(st3)

#difference

st4=st.difference(st1)
print(st4)
#element should be present in first set does not present in second set

st5=st1.difference(st)
print(st5)