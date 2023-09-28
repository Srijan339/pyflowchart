s=int(input())
a=int(input())
d=int(input())
m=int(input())

if a<(0.8*s):
    print("Sorry, you do not qualify for the special discount on membership renewal.")
    print("(Attendance<80%)")
elif d==1:
    print("Sorry, you do not qualify for the special discount on membership renewal.")
    print("(Outstanding payments)")
elif m<6:
    print("Sorry, you do not qualify for the special discount on membership renewal.")
    print("(Not a member for at least 6 months)")
else:
    print("Congratulations! You qualify for the special discount on membership renewal.")
    
