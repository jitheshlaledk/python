number_of_class=int(input("enter number of classe held"))
attended_number_of_class=int(input("enter attended number of class"))

percentage=(attended_number_of_class/number_of_class)*100

if(percentage>75):
    print("allowed for exam")
else:
    print("not allowed")
