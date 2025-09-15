# Built in string functions
q = "Bottle"
print(len(q))

w = " hello world "
print(w.strip())

e = "Skipping"
print(e.lower())
print(e.upper())
 
r = "hi im fine"
print(r.find("fine"))
print(r.find("grape"))

t = "i love apples"
print(t.replace("apples","bananas"))

y = "bananas"
print(y.count("a"))

u  = "canteloupe,watermelon,apple"
print(u)
# print(u.split("$"))

i = "card"
print(i.capitalize())

print("book".isalpha())

print("1234".isdigit())
print("book".isdigit())

print("300chickens".isalnum())



# Escape sequence


# 1 New line
print("hello\nworld")


# tab
print("name:\tdavid")


# Backslash
print("this is a backslash \\")


# Single quote
print('david\'s')


# double quotes
print("She said \"hi\"")
