import requests, jsonify

print(requests.get("http://127.0.0.1:5000").content.decode())
print(requests.get("http://127.0.0.1:5000").content.decode())

print(check_fields({}, {'id', 'quantity'}))
print(check_fields({'id':0}, {'id', 'quantity'}))
print(check_fields({'id': 0, 'quantity': 0}, {'id', 'quantity'}))
print(check_fields({'id':0, 'quantity':0, 'description':""}, {'id', 'quantity'}))

req = requests.post("http://127.0.0.1:5000/cart", json={
    'id': "azeezrzerd"
})
print(req.status_code, req.json())


req = requests.post("http://127.0.0.1:5000/cart", json={
    'id' : "qefsderf",
    'quantity': 3
})
print(req.status_code, req.json())


req = request.get("http://127.0.0.1:5000/cart",).json()
print(req)


requests.post("http://127.0.0.1:5000/cart", json={
    'id' : "aqasdvb",
    'quantity': 1
})

requests.post("http://127.0.0.1:5000/cart", json={
    'id' : "aqasdvb",
    'quantity': 3
})

req = request.get("http://127.0.0.1:5000/cart",).json()
print(req)

req = requests.patch("http://127.0.0.1:5000/cart", json={
    'id': "aaaaa",
    'quantity': 10
})
print(req.status_code, req.json())

req = requests.patch("http://127.0.0.1:5000/cart", json={
    'id': "je8zng",
    'quantity': 10
})
print(requests.get("http://127.0.0.1:5000/cart").json())