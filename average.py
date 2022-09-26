a=int(input("enter your tamil marks"))
b=int(input("enter your english marks"))
c=int(input("enter your maths marks"))
d=int(input("enter your science marks"))
e=int(input("enter your social marks"))
Total=a+b+c+d+e
print("Total:",Total)
Average=Total/5
print("Average:",Average)
if a & b & c & d & e >= 35:
    print("Each subject is above:35")
    if Average>35:
     print("pass")
    if Average<=100 and Average>=90:
     print("grade A")
    if Average<=89 and Average>=80:
     print("grade B")
    if Average<=79 and Average>=70:
     print("grade C")
    if Average<=69 and Average>=60:
     print("grade D")
    if Average<=59 and Average>=50:
     print("grade E")


else:
    print("fail")


