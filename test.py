import time
print("Hello World")
print(13 // 4)
print(time.time()/(365*24*60*60))

# NL

# Formatting Strings

print("Hello %s" % "world")
print("%r" % "hi\n") # Repr (Uses Repr())
print("%o" % 8) # -> 10 Octal
print("%x" % 255) # -> 16 Hex
print("%.2f" % 3.14159) # -> 3.14 Fix Float
print("%E" % 1424124) # Scientific Notation
print("%c" % 65) # -> A unicode character set ASCII
print("%d" % 25.0) # -> Integer
print("%g" % 25) # -> float

# String Slicing
# Segment of a string is a "slice"
word = "Daniel Milde"
slice = word[5:10]
print(slice)

# String Slicing Step Size
slice2 = word[0::3]# Gets ltters 0 and 3
print(slice2)

slice3 = word[0:2:12] # Step Size
print(slice3)

# Negative Indexing??
print(word[-1])

print(word[-1::-2])
print(word[::-2])
# These Two are the SAME! ^^^
