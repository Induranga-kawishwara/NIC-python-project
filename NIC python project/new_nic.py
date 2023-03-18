def nic(user,userin):
    #outputs
    print("your NIC number is:-- New")
    print("your birth year is :-- "+user[0:4])
    def sex(userin):
            if userin[4:7]>=["0","0","1"] and userin[4:7]<=["3","6","6"]:
                return "a male"
            else:
                return "a female"
    print("your are",sex(userin))#call funtion
