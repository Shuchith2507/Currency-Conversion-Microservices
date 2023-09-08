# Microservices-Based-Architecture


Converted a monolith architecture based docker-compose application into a microservices based architecture.


To run just execute:
docker compose up


This is run all microservices running in different ports virtulized to the landing page's port(5050)

This is basically currency conversion from INR to different currency



The directory structure of every microservice:

├── <name of the service>
  
│   ├── Dockerfile          
  
│   ├── app
  
│   │   ├── app.py          \
  
│   │   └── requirements.txt # same as landing/app/requirements.txt
  
│   │  
  
  


