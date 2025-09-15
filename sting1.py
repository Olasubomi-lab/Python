a = "r"
print(a)

b = 'r'
print(b)

c = """r"""
print(c)

d = """Sports encompass physical activities, from individual pursuits like running to team endeavors like football, 
offering numerous benefits such as improved physical and mental health, enhanced social skills like teamwork and discipline,
 and the fostering of community spirit. Engaging in sports provides both active participants and enthusiastic spectators with enjoyment,
 a sense of accomplishment, and opportunities to learn resilience, cooperation, and respect for rules and opponents"""

e = "gregory"
print(e)

f = "37"
print(f)
print(type(f))





# Slicing of a string
# Method 1 - using slice

g = "Rectangle"
h = slice(3)
print(g[h])

i = slice(1,4)
print(g[i])

j = slice(1,4,3)
print(g[j])

k = slice(1,6,2)
print(g[k])

l = slice(2,7,3)
print(g[l])

m = slice(-1,-9,-2)
print(g[m])


# method 2 - Using array slicing

z = "dictionary"
print(z[:])

print(z[0:3])

print(z[2:])

print(z[:5])

print(z[0:7:2])

print(z[::2])

print(z[::-1])
