
year = int(input("Enter The Year: "))


if(year % 4 == 0 and year % 100 != 0 or year % 400==0):
    print('This is a Leap Year')

else:
    print('This is not a Leap Year')



hic = int(input("Enter the hight in centimeters: "))

inc = 0.394*hic

feet = 0.0328*hic

print("The hight in inches is: ",round(inc,2))

print("The hight in feet is: ",round(feet,2))