from requests import get, post, delete

print(post('http://localhost:5000/api/jobs').json())  # ничего не отправлляется

print(post('http://localhost:5000/api/jobs', json={}).json())  # отправляется пустой json-файл

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 5}).json())  # отправляется json-файл с недостаточным количеством данным

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 2,
                 'job': 'life search',
                 'collaborators': '3, 4, 5',
                 'is_finished': False,
                 'work_size': 26,
                 'id': 7}).json())  # отправляется json-файл с уже существующим id

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'development of new schedule',
                 'collaborators': '1, 2',
                 'is_finished': True,
                 'work_size': 39}).json())  # корректный запрос

print(get('http://localhost:5000/api/jobs').json())  # получение всех работ

