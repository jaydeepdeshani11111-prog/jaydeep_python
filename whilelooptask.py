#1.print number from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1

#2.sum of nummbers take user input.
n = int(input("Enter a number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum is:", total)

#3.print odd number between 1 and 20.
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

#4.print table of 4.
i = 1
while i <= 10:
    print("4 x", i, "=", 4 * i)
    i += 1

#5.print reverse number.
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse number is:", reverse)

#6.find largest number in list.
numbers = [10, 45, 23, 89, 67]

i = 0
largest = numbers[0]

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print("Largest number is:", largest)

#7.print even number between 1 and 20.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
