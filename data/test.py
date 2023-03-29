from requests import get

print(get('http://localhost:5000/api/jobs').json())
print()

print(get('http://localhost:5000/api/jobs/1').json())
print()

print(get('http://localhost:5000/api/jobs/34').json())
print()

print(get('http://localhost:5000/api/jobs/h').json())
