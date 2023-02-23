import requests
import json


class Tarefa():
    def __init__(self, task, description) -> None:
        self.task = task
        self.description = description

# Recuperar dados da API
def get():
    request = requests.get("http://localhost:3002/api/todo")

    tasks = json.loads(request.content)

    for task in tasks:
        print('TaskName: ', task['task'], '; ', 'Description: ', task['description'])

# Cadastrar dados na API
def post(taskObject):

    r = requests.post(
            'http://localhost:3002/api/todo', 
            data=json.dumps(taskObject.__dict__)
        )
    print(r.text)

# Atualizar dados na API
def put(id, taskObject):
    requests.put(
            f'http://localhost:3002/api/todo?id={id}',
            data=json.dumps(taskObject.__dict__)
        )

# Removendo dados da API
def delete(id):
    requests.delete(
        f'http://localhost:3002/api/todo?id={id}'
    )

if __name__ == '__main__':
    # post(Tarefa('Estudar API', 'Estudar API com Python e tw-dev-server'))
    # post(Tarefa('Estudar MySQL', 'Estudar MySQL com python e JavaScript'))
    get()