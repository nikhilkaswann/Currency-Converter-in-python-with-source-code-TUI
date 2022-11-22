list1=["0","Indian Rupee(INR)","United States Dollar(USD)","Euro(EUR),Canadian Dollar(CAD)","Chinese Yuan(CNY)","Russian Ruble(RUB)","Pakistani Rupee(PKR)","United Arab Emirates Dirhan(AED)"]
print("FROM (type no. for choosing currency)\n 1 for Indian Rupee(INR) \n 2 for $ United States Dollar(USD) \n 3 for Euro(EUR) \n 4 for Canadian Dollar(CAD)\n 5 for Chinese Yuan(CNY)\n 6 for Russian Ruble(RUB) \n 7 for Pakistani Rupee(PKR) \n 8 for United Arab Emirates Dirhan(AED)")

f = int(input("FROM : "))
if 0<f and f<9:
    print("TO (type no. for choosing currency)\n 1 for Indian Rupee(INR) \n 2 for $ United States Dollar(USD) \n 3 for Euro(EUR) \n 4 for Canadian Dollar(CAD)\n 5 for Chinese Yuan(CNY)\n 6 for Russian Ruble(RUB) \n 7 for Pakistani Rupee(PKR) \n 8 for United Arab Emirates Dirhan(AED)")
    t = int(input("TO : "))
    print(list1[f], "to", list1[t])
    if 0<t and t<9:
        a=float(input("Enter your amount " ))
        ###INR f==1

        if f ==1 and t== 1:
            p=(a*1)
        elif f==1 and t==2:
            p=(a*0.012)
        elif f==1 and t==3:
            print(a*0.012)
        elif f==1 and t==4:
            p=(a*0.016)
        elif f==1 and t==5:
            p=(a*0.088)
        elif f==1 and t==6:
            p=(a*0.75)
        elif f==1 and t==7:
            p=(a*2.74)
        elif f==1 and t==8:
            p=(a*0.045)

        ###USD f==2

        elif f == 2 and t == 1:
            p=(a*81.75)
        elif f == 2 and t == 2:
            p=(a*1)
        elif f == 2 and t == 3:
            p=(a*0.97)
        elif f == 2 and t == 4:
            p=(a*1.34)
        elif f == 2 and t == 5:
            p=(a*7.15)
        elif f == 2 and t == 6:
            p=(a*60.66)
        elif f == 2 and t == 7:
            p=(a*223.93)
        elif f == 2 and t == 8:
            p=(a*3.67)

        ###EUR F==3

        elif f == 3 and t == 1:
            p=(a*83.88)
        elif f == 3 and t == 2:
            p=(a*1.03)
        elif f == 3 and t == 3:
            p=(a*1)
        elif f == 3 and t == 4:
            p=(a*1.38)
        elif f == 3 and t == 5:
            p=(a*7.35)
        elif f == 3 and t == 6:
            p=(a*62.26)
        elif f == 3 and t == 7:
            p=(a*229.82)
        elif f == 3 and t == 8:
            p=(a*3.77)

        ###CAD F==4
        elif f == 4 and t == 1:
            p=(a*60.87)
        elif f == 4 and t == 2:
            p=(a*0.74)
        elif f == 4 and t == 3:
            p=(a*0.73)
        elif f == 4 and t == 4:
            p=(a*1)
        elif f == 4 and t == 5:
            p=(a*5.33)
        elif f == 4 and t == 6:
            p=(a*45.16)
        elif f == 4 and t == 7:
            p=(a*166.72)
        elif f == 4 and t == 8:
            p=(a*2.73)


        ###RUB F==5
        elif f == 5 and t == 1:
            p=(a*11.42)
        elif f == 5 and t == 2:
            p=(a*0.14)
        elif f == 5 and t == 3:
            p=(a*0.14)
        elif f == 5 and t == 4:
            p=(a*0.19)
        elif f == 5 and t == 5:
            p=(a*1)
        elif f == 5 and t == 6:
            p=(a*8.57)
        elif f == 5 and t == 7:
            p=(a*31.30)
        elif f == 5 and t == 8:
            p=(a*0.51)

        ### F==6

        elif f == 6 and t == 1:
            p=(a*1.35)
        elif f == 6 and t == 2:
            p=(a*0.016)
        elif f == 6 and t == 3:
            p=(a*0.016)
        elif f == 6 and t == 4:
            p=(a*0.022)
        elif f == 6 and t == 5:
            p=(a*0.12)
        elif f == 6 and t == 6:
            p=(a*1)
        elif f == 6 and t == 7:
            p=(a*3.69)
        elif f == 6 and t == 8:
            p=(a*0.061)

        ### F==7

        elif f == 7 and t == 1:
            p=(a*0.37)
        elif f == 7 and t == 2:
            p=(a*0.0045)
        elif f == 7 and t == 3:
            p=(a*0.0044)
        elif f == 7 and t == 4:
            p=(a*0.0060)
        elif f == 7 and t == 5:
            p=(a*0.032)
        elif f == 7 and t == 6:
            p=(a*0.27)
        elif f == 7 and t == 7:
            p=(a*1)
        elif f == 7 and t == 8:
            p=(a*0.16)

        ###AED f==8
        elif f == 8 and t == 1:
            p=(a * 22.25)
        elif f == 8 and t == 2:
            p=(a * 0.27)
        elif f == 8 and t == 3:
            p=(a * 0.27)
        elif f == 8 and t == 4:
            p=(a * 0.37)
        elif f == 8 and t == 5:
            p=(a * 1.92)
        elif f == 8 and t == 6:
            p=(a * 16.51)
        elif f == 8 and t == 7:
            p=(a * 60.92)
        elif f == 8 and t == 8:
            p=(a * 1)
        print(a,list1[f],"is",p, list1[t])

    else:
        print("currency not in currency converter")
else:
    print("currency not in currency converter")



