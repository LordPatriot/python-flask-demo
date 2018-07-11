Image available [here](https://hub.docker.com/r/mozorbo/python-flask-demo/).

You can build *your own image* with *your own flask app* like that:
- Clone this repo: ```git clone https://github.com/LordPatriot/python-flask-demo.git```
- ```cd ./python-flask-demo/docker```
- In this folder, substitute ```app.py``` with your own flask app or simply change the message from *Hello, world* to *Hi there* for testing purposes
- ```docker build -t <YOUR_IMAGE_NAME> .``` (given that Docker is installed and configured on your machine)
- ```docker run -t <YOUR_IMAGE_NAME>```
