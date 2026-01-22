# def greet(name = "Manvith"):
#  return (f"Hello {name}!")

 #msg = greet()
#print(msg)

#MULTIPLE PARAMETERS

#def add(x, y):
 #   return x+y

#sum = add(x = 0, y = 0)
#print(sum)

#FUNCTIONS WITH LOOP

def running_nums(nums):
    total = 0
    result = []
    for i in nums:
        total += i
        result.append(total)
    return(result)
    
print(running_nums([6, 7, 8, 9, 10]))
