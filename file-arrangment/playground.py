file = open("demo.txt", "w")

for idx in range(1, 6):
	name = input("Enter your name: ")
	age = input("Enter your age: ")

	file.write(f"{idx} {name}, {age}\n")

file.close()


with open("names-text", "w") as file1:
	file1.write("1. maxi wisdom")


try:
	with open("deme.text", 'r') as file2:
		names = file2.read()
		print(names)
except FileNotFoundError:
	print("File not found")

finally:
	file2.close()

