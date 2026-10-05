num1=float(input("enter the first number:"));
num2=float(input("enter the second number:"));
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
choice=int(input("enter your choice(1-4):"))
if choice==1:
    print("result=",num1+num2);
elif choice==2:
    print("result=",num1-num2);
elif choice==3:
    print("result=",num1*num2);
elif choice==4:
    if num2!=0:
        print("result=",num1/num2);
else:
    print("Division by zero is not possible");

