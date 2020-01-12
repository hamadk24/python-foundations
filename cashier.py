items_list = []

itemList = input("Item (enter 'done' when finished!): ")
while itemList != "done":
	itemPrice = float(input("Price: "))
	itemQuantity = int(input("Quantity: "))
	items_dictionary = {
		"name": itemList,
		"price": itemPrice,
		"quantity": itemQuantity
	}
	items_list.append(items_dictionary)
	itemList = input("Item (enter 'done' when finished): ")
print("!!!!!!!!!!!!")
print("Le Receipt Monsewer")
print("!!!!!!!!!!!!")

total = 0
for item in items_list:
	print(f'{item["quantity"]} {item["name"]} {item["price"] * item["quantity"]}KWD')
	total += item['price'] * item['quantity']

print(f"Final Price: {total}KWD")