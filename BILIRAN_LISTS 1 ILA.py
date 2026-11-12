items = []
print("Enter 5 items:")
for i in range(5):
  val = input(f"Item {i + 1}: ")
  items.append(val)


print("Original List: ", end="")
for i in range(len(items)):
  print(items[i], end=", ")
print() 

indexup = int(input("Input Index to Update: "))
new_value = input("Input New Value: ")

if 0 <= indexup < len(items):
  items[indexup] = new_value
else:
  print("Invalid index! Skipping update.")

print("Updated List: ", end="")
for i in range(len(items)):
  print(items[i], end=", ")
print()

slice_1 = int(input("Enter Slice Range 1: "))
slice_2 = int(input("Enter Slice Range 2: "))

sliced_list = items[slice_1:slice_2]
print("Sliced List: ", end="")
for item in sliced_list:
  print(item, end=", ")
print()

search_item = input("Enter Search Item: ")
found = False

for i in range(len(items)):
  if items[i].lower() == search_item.lower():
    print(f"Result: '{items[i]}' was found at index {i}.")
    found = True
    break

if not found:
  print(f"Result: '{search_item}' was not found in the list.")