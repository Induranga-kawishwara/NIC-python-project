import old_nic
import new_nic
#craete variables
userin=[]
user=''
#processing parts
print("__________***welcome***__________\n".center(70))
user=input("\nEnter you NIC number:")
userin=list(user)
if len(user)==10:
    if user[-1]== "v" or user[-1]== "x":
        old_nic.nic(user,userin)#call funtion
    else:
        print("Your NIC number is invalided")#output  
else:
    if len(user)==12:
        try:
            int(user)
            new_nic.nic(user,userin)#call funtion
        except ValueError:
            print("Your NIC number is invalided")
    else:
        print("Your NIC number is invalided")#output
