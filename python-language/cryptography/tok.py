import jwt

data = {'payload': 'data', 'id': 123456789}

token = jwt.encode(data, 'secret-key')
data_out = jwt.decode(token, 'secret-key')
print(token)
print(data_out)

print("====================================")

token512 = jwt.encode(data, 'secret-key', algorithm='HS512')
data_out = jwt.decode(token512, 'secret-key', algorithms='HS512')
print(token512)
print(data_out)

#print(jwt.decode(token, verify=False))