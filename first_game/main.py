print("Welcome to my first Game!")

name = input("Tell me your name.\n")
age = int(input("And your age is ?\n"))

print("Hello", name, "that is", age, "years old,")

if age > 12:
	print("\nWelcome to Pythoria, ready to start your adventure? \n")

	answer1 = input("(yes or no) \n").lower()

	if answer1 == "yes":
		print("GREAT!")
	else:
		print("SAD")

else:
	print("\nI'm sorry but you're too young for adventure, at least this one.")

