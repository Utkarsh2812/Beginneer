def reverse(n, r = 0):
    if n == 0:
        return r
    else:
        return reverse(n//10 , n%10 + r*10)     #Applying pallindrome concept skipping the check
    
n = int(input("Enter the Number: "))
r_n = reverse(n)
print(f"Reverse of {n} is {r_n}")