person = {"name":"sumedh" ,"gender":"male","age":"22" , "address":"mayur nagar", }
k= input("information required    ").lower()
result = person.get(k, "that is not avaliable")
print(result)
