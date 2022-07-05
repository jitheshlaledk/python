st={10,20,30,40,50,60,70,80,90,100}
print(st)

#delete a element in set

st.remove(50)
print(st)

st.discard(20)
print(st)

#difference between remove and discard

#remove is return type
#discard is not return type(no change if element is not present in that set)
