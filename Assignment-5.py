#Q.1-Take an input year from user and decide whether it is a leap year or not
 
year=int(input("enter a year for leap year check:"))
if year%4==0:
    print("year is leap year")
else:
   print("year is not a leap year")
print("\n")

#Q.2-Take length and breadth input from user and check whether the dimensions are of square or rectangle.

l=int(input("enter the length"))
b=int(input("enter the breadth:"))
if l==b:
   print("entered dimension are of square")
else:
    print("entered dimension are of rectangle")
print("\n")


#Q.3-Take the input of 3 people and determine oldest and youngest among them.
 
a=int(input("enter age of person a: "))
b=int(input("enter age of person b: "))
c=int(input("enter age of person c: "))


if a>b:
	if a>c:
		print("a is oldest")
	else:
		print("c is oldest")
else:
	if b>c:
		print("b is oldest")
	else:
		print("c is oldest")
	
		

if a<b:
	if a<c:
		print("a is youngest")
	else:
		print("c is youngest")
else:
	if b<c:
		print("b is youngest")
	else:
		print("c is youngest")
print("\n")

#QUESTION -4 		
score=int(input("enter a score"))
if score<=50:
	print("sorry no prizes")
else:
	if score<=150:
		print("congratulation! you've won wooden dog")
	else:
		if score <=180:
			print("congratulation! you've won books")
		else:
			print("congratulation! you've won chocolates")
print("/n")


# Q-5 A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 

q=int(input("enter a purchase quantity: "))
c=q*100
if c>=1000:
	print("you are eligible for discount:")
	d=(c*10)/100
	p=c-d
	print("your total cost is:",p)
else:
	print("you are not eligible for discount")
	
		
			
		   
	   
	
	
	
	