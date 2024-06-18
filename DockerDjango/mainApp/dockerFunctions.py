import docker

#Change these values to the values required for your project
healthcheckDict = {
    "test": ["CMD-SHELL", "curl -f http://localhost/ || exit 1"],
    "interval": 5000000,
    "timeout": 5000000,
    "retries": 3,
    "start_period": 5000000
}
#dockerClient = docker.DockerClient()

client = docker.from_env()

# Connect to different Docker hosts dynamically by specifying host URL and port
# def connect_to_docker(host, port):
#     return DockerClient(base_url=f"http://{host}:{port}")

#This runs the command with the image and 
print(client.containers.run("alpine", ["echo", "hello", "world"]))

#Get and return a list of container. Also filters out the 
# containers built with a given image name
def getContainers(imageName):
    containersList = []
    containers = client.containers.list(all=True)
    for container in containers:
        if imageName in str(container.image):
            containersList.append(container)
    return containersList

#List all containers with no filtering
def allContainers():
    containersList = client.containers.list(all=True)
    return containersList

#Print all info for conatiners in list
def containersInfo(containerList):
    for container in containerList:
        print(f"ID: {container.id}, Name: {container.name}, Image: {container.image.tags}")

#Delete all containers
def removeAllContainers():
    containers = allContainers()
    for container in containers:
        try:
            container.stop()
            container.remove()
            # Add exception handling here so that if the container refuses to 
            # stop we do not run into an error!!!
        except Exception as e:
            print("##############Error Stopping Container##############")
            print(container.name)
            print(e)
    client.containers.prune()  #dockerClient.containers.prune()

#Delete specific container
def removeContainer(containerName):
    containers = allContainers()
    for container in containers:
        if containerName in str(container.image):
            print("##############Deleting##############")
            print(container.name)
            try:
                container.stop()
                container.remove()
            except Exception as e:
                print("##############Error Deleting Container##############")
                print(container.name)
                print(e)

#Get the container stats
def containerStats(containerName):
    container = client.containers.get(containerName)
    stats = container.stats(stream = False)
    print(stats)

# Pauses all processes within this container
def pause(container):
    pause(container)

#Build Image and Start Containers (Start from existing image or create image if it does not exist)
def runContainer(imageName, command=None):
    #run(image, command=None, **kwargs)
    try:
        client.containers.run(image=imageName, command=command, detach=True, healthcheck = healthcheckDict)
        print("Successfully started!")
    except Exception as e:
        print(f"Something went wrong! Error: {e}")