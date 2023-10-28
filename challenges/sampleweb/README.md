# Sampleweb installation

This is an example of a multi-container service for iCTFd.

In order to install it, you first need to find a host on which the service will run, becuase iCTFd does not support multi-container services.
For the sake of this example, let's assume that the host is 10.10.10.10.

You need to copy the files on 10.10.10.10 and install docker and docker-compose.
On Ubuntu:
% sudo apt-get install docker docker-compose

Also you need to add your account to the right group:
% sudo groupadd docker
% sudo usermod -aG docker ${USER}

and then logout and log back in.
To check that everything is OK you can run:
% docker run hello-world

To build the service:
sampleweb% docker-compose build

To run the service:
sampleweb% docker-compose up

To run the service in the background:
sampleweb% docker-compose up -d
