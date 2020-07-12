lotnumber = input("enter 12digit product lot number in  form _ _ _-_ _ _ _ _-_ _ _ _ _")
print("country code", lotnumber[:3])
print("product code", lotnumber[4:9])
print("batch code", lotnumber[10:])
