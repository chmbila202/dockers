# dockers
Cncpts &amp; Strctrs:Intrnt Cmptng Assignment 5 
Created a flask JSON RESTful Web Service and Run it inside docker containers
Designed the Flask RESTful Web Service
Created datebase design and add data
Created Flask webservice
Deployed the database inside MySQL Container
Deployed the Flask web Service inside Flask Container
Test application using host machine
Database name “docker”
Two tables i.e., customer and orders
Customer contain multiple customers
Orders contain multiple orders produced by the customers
/customer
List all customers with ID
/customer/<cid>
Give details of the customer with ID = <cid>
/customer/<cid>/orders
Give list of order ids created by the customer id
/customer/<cid>/orders/<oid>
Give the list of order id and item details of specific order id
  my dockers container:
  docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=abc123 -d mysql
Connected the machine with SQL Editor such as HeidiSQL
Deployed the database
Checked the ip address of the docker machine using docker inspect mysql [docker_mysql_ip]
  flask docker container:
  Create requirements file in pycharm project
Create dockerfile in  pycharm project
Insert docker mysql ip address in flask project
Build the project 
docker image build -t docker-flask .
Run project
docker run -it -p 5001:5001 -d docker-flask
![image](https://user-images.githubusercontent.com/35162681/174241501-4d1ce9ac-d7b0-40ce-813f-5a6e04474cea.png)

![image](https://user-images.githubusercontent.com/35162681/174241378-81b139be-b152-4f7d-81a8-2facaf23cc92.png)

![image](https://user-images.githubusercontent.com/35162681/174241305-5e34c1ce-adcd-47c8-b548-4d757f7dc812.png)

![image](https://user-images.githubusercontent.com/35162681/174241263-eea0000a-efb4-4335-ad06-a7f5bb717259.png)

![image](https://user-images.githubusercontent.com/35162681/174241162-806092cb-db67-415e-8731-862de41b69f3.png)

![image](https://user-images.githubusercontent.com/35162681/174241093-3c7902cd-d044-4a10-901d-1657a6881a78.png)
