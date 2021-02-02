import requests


if __name__ == '__main__':
    response = requests.post(
        url='http://localhost:8000/h1st/models/exec/',
        auth=('<username>', '<password>'),
        headers={'Content-Type': 'application/json'},
        json={
            'UUID': '<UUID of Workflow>',
            'a': 1, 'b': 2, 'c': 3   # input data
        })

    print(response.text)
