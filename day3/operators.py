# Day 3: 30 Days of Python Programming

# Basic variables
age = 23
height = 1.75
complex_number = 5 + 6j


# Area of a triangle
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_triangle = 0.5 * base * height
print(f"The area of the triangle is {int(area_triangle)}")


# Perimeter of a triangle
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_triangle = a + b + c
print(f"The perimeter of the triangle is {perimeter_triangle}")


# Area and perimeter of a rectangle
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(
    f"The area of the rectangle is {area_rectangle} "
    f"and the perimeter is {perimeter_rectangle}"
)


# Area and circumference of a circle
radius = int(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius ** 2
circumference = 2 * pi * radius
print(
    f"The area of the circle is {int(area_circle)} "
    f"and the circumference is {int(circumference)}"
)


# Slope and intercepts of y = 2x - 2
slope = 2
x_intercept = -2 / 2
y_intercept = -2
print(
    f"The slope is {slope}, "
    f"the x-intercept is {x_intercept}, "
    f"and the y-intercept is {y_intercept}"
)


# Slope and Euclidean distance between (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_points = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(
    f"The slope is {slope_points} "
    f"and the Euclidean distance is {euclidean_distance}"
)

if slope_points > euclidean_distance:
    print("The slope is greater than the Euclidean distance")
else:
    print("The slope is less than the Euclidean distance")


# Calculate y = x² + 6x + 9
x = int(input("Enter x: "))
y = x ** 2 + 6 * x + 9
print(f"The value of y is {y}")


# Length comparison of strings
python_len = len("python")
dragon_len = len("dragon")

print(
    f"The length of python is {python_len} "
    f"and the length of dragon is {dragon_len}"
)

print(python_len != dragon_len)

print("on" in "python" and "on" in "dragon")


# String checks
sentence = "I hope this course is not full of jargon."
print(len(sentence))
print("jargon" in sentence)
print("on" in sentence)


# Convert length to float and string
text_length = len("Hello from the other side")
text_length = str(float(text_length))


# Check odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# Floor division check
print(7 // 3 == int(2.7))
print(type("10") == type(10))


# Weekly earning
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
earning = hours * rate
print(f"Your weekly earning is {earning}")


# Seconds lived
years = int(input("Enter number of years you have lived: "))
seconds_lived = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds")


# Display table
for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)
