import docker

client = docker.DockerClient()
print(client.containers)
container = client.containers.get('db')
ip_add = container.attrs['NetworkSettings']['IPAddress']
print(ip_add)

class db:
    hostname = f'{ip_add}:5432'
    username = 'postgres'
    password = 'kSqHwjRhBOHIwU'