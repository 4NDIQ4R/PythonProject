import socket
import requests
url = 'https://brickset.com/sets/year-2015'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t *", r.status_code)
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
headers = {
    'User-agent': 'Mobile'
}

HOST, PORT = "", 8080,
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(True)

print("Serving HTTP on port %s.." % PORT)

while True:
    client_connection, client_address = s.accept()
    request = client_connection.recv(1024) # Buffer Size
    print(request.decode("utf-8"))  # Display the HTTP request
    http_response = """/

HTTP/1.1 200 OK

Welcome to Group 6 !
"""
    client_connection.sendall(bytes(http_response, "utf-8"))
    client_connection.close()
