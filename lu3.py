                 #Conditional operators and loops exercise
#1.To write a program that inputs n integers (n > 0) and finds the largest among them.
#First, the number of numbers n is entered. Then n integers are entered
#First way:
n = int(input("Въведете броя на числата: "))
if n > 0:
    numbers = []
    for i in range(n):
        number = int(input(f"Въведете число {i + 1}: "))
        numbers.append(number)

    max_number = max(numbers)
    print(f"Най-голямото число е: {max_number}")
else:
    print("Моля, въведете валиден брой числа (n > 0).")
#second way for this exercise    
n = int(input("vuvedete broq na chislata: "))
max_number = -100
for i in range(n):
    number =int(input(f"vuvedete chislo {i+1}: "))
    if number>max_number:
        max_number=number
print(max_number)

#2. To write a program that inputs n integers and sums them

n = int(input("Въведете брой на целите числа: "))
suma = 0

for i in range(n):
    chislo = int(input(f"Въведете цяло число #{i + 1}: "))
    suma += chislo

print(f"Сумата на въведените числа е: {chislo}")

#3. To write a program that enters a number n
#and prints a triangle of asterisks

n=int(input("Enter a number   "))
for i in range(1,n+1):
    print("*" *n)


#4. Write a program that checks whether a given number is prime,
#the number is entered by the user.
n=int(input("Enter a number  "))
delitel= 2
while delitel<n:
    if n%delitel==0:
        print(f"chisloto {n} ima delitel{delitel} i ne e prosto")
        break
    delitel+=1
else:
    print(f"chisloto {n}  e prosto")
