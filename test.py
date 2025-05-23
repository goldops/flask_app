import requests

print(requests.get("http://127.0.0.1:5000").content.decode())
print(requests.get("http://127.0.0.1:5000").content.decode())

print(check_fields({}, {'id', 'quantity'}))
print(check_fields({'id':0}, {'id', 'quantity'}))
print(check_fields({'id': 0, 'quantity': 0}, {'id', 'quantity'}))
print(check_fields({'id':0, 'quantity':0, 'description':""}, {'id', 'quantity'}))