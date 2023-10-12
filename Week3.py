from typing import List, Any

marks = []
mark = input("Enter mark one")
marks = marks +[mark]
mark = input("Enter mark two")
marks = marks +[mark]
mark = input("Enter mark three")
marks = marks +[mark]
mark = input("Enter mark four")
marks = marks +[mark]
mark = input("Enter mark five")
marks = marks +[mark]
print("Marks are : ")
print(marks)
print("highest is ", max(marks))
print("lowest is ", min(marks))
