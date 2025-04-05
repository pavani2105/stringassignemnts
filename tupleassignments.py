# Tuple Creation  
t = (10, "Hello", 3.14, "World", 45)  
print("Original Tuple:", t)  

# Accessing Elements  
print("First Element:", t[0])  
print("Last Element:", t[-1])  
print("Second Last Element:", t[-2])  

# Tuple Slicing  
print("First Three Elements:", t[:3])  
print("Last Two Elements:", t[-2:])  

# Tuple Operations  
u = ("Python", "Programming")  
v = t + u  
print("Concatenated Tuple:", v)  

w = t * 2  
print("Repeated Tuple:", w)  

# Tuple Methods  
x = t.index("Hello")  
print("Index of 'Hello':", x)  

y = t.count(10)  
print("Occurrences of 10:", y)  

# Tuple Immutability  
try:  
    t[1] = "Changed"  # This will raise an error  
except TypeError as e:  
    print("Error:", e)  
print("Tuples are immutable. You cannot change their elements.")  

# Tuple Packing and Unpacking  
p = ("Apple", 50, 9.99)  
a, b, c = p  
print("Unpacked Values:", a, b, c)  

# Tuple Iteration  
print("Iterating through t:")  
for element in t:  
    print(element)  

# Tuple Usage  
def return_values():  
    return ("Value1", "Value2", "Value3")  

r = return_values()  
print("Returned Tuple:", r)  
