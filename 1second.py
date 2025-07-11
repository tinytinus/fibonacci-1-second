from time import * 

start_time = time()

n1 = 0
n2 = 1
j = 0

while time() <= start_time + 1:
    n = n2+n1
    n1 = n2
    n2 = n
    j += 1

print ("time:", (time() - start_time) ,"\n")

print_time = time()

chunks = []
remaining = n
while remaining > 0:
    remaining, chunk = divmod(remaining, 10**10)
    chunks.append(chunk)

number = "".join("%010d"%chunk for chunk in reversed(chunks))

length = len(number)

print ("the", j, "'th fibonacci number is", number, " \n")
print ("that is" , length , "charchters long!! \n")

print ("time taken for printing: ", (time() - print_time), "\n")
    
    
    

