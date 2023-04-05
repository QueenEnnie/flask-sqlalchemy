from requests import get, post

# print(get('http://localhost:5000/api/jobs').json())
# print()
#
# print(get('http://localhost:5000/api/jobs/1').json())
# print()
#
# print(get('http://localhost:5000/api/jobs/34').json())
# print()
#
# print(get('http://localhost:5000/api/jobs/h').json())

print(post('http://localhost:5000/api/jobs').json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 5}).json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 2,
                 'job': 'life search',
                 'collaborators': '3, 4, 5',
                 'is_finished': False,
                 'work_size': 26,
                 'id': 7}).json())
