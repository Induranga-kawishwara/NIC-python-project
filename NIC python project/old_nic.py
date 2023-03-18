def nic(user,userin):
    #outputs
    print("your NIC number is:-- OLD")
    print("your birth year is :-- 19"+user[0:2])
    def sex(userin):
            if userin[2:5]>=["0","0","1"] and userin[2:5]<=["3","6","6"]:
                return "a male"
            else:
                return "a female"
    print("your are",sex(userin))#call funtion
    def vol(userin):
        if userin[-1]== "v":
            return "voter"
        else:
            return "Non-voter"
    print("you are a",vol(userin))#call funtion   
    
        
