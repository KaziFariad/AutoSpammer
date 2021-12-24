s = input("Enter a message:")

with open("message.txt", "w") as file:
  for i in range(10):
    file.write(s)
    file.write("\n")