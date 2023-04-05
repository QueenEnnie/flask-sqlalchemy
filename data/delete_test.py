from requests import get, delete

print(get('http://localhost:5000/api/jobs').json())

print(delete('http://localhost:5000/api/jobs/999').json())

print(delete('http://localhost:5000/api/jobs/j').json())

print(delete('http://localhost:5000/api/jobs/9f').json())

print(delete('http://localhost:5000/api/jobs/10').json())

print(get('http://localhost:5000/api/jobs').json())
