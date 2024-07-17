# Microservice Documentation

This repository contains a microservice developed using Python, Flask, MongoDB, and deployed on Kubernetes. The microservice includes authentication, CRUD operations, configuration management, status & health checks, error handling, and containerization.

## Setup

### Prerequisites

- Python 3.x
- Docker
- Kubernetes (optional for deployment)

### Installation

1. Clone the repository:
   git clone https://github.com/ajinkya-mohite/microservice.git
   cd microservice

2. Install dependencies:
   pip install -r requirements.txt

3. Set up MongoDB:
   Ensure MongoDB is running locally or update config.py with your MongoDB URI.

4. Build the Docker image:
   docker build -t microservice-python .

   Run the Docker container:
   docker run -d -p 5000:5000 --name microservice-container microservice-python

5. Usage
   Local Development: The microservice can be run locally for development purposes using Flask's built-in server.
   Ensure MongoDB is running and update config.py with the correct URL.
   python app.py

   Endpoints:

   /login
    POST: Authenticates a user with username and password. Returns an access token.

   /item
    GET: Retrieves all items.
    POST: Creates a new item.

   /item/<item_id>
    GET: Retrieves a specific item by ID.
    PUT: Updates an existing item by ID.
    DELETE: Deletes an item by ID.

  /health
   GET: Checks the health status of the microservice.

6. Deployment on Kubernetes:
   -Ensure Kubernetes is set up and kubectl is configured to the correct cluster.
   -Apply the Kubernetes deployment configuration:
             kubectl apply -f deployment.yaml
   -Verify deployment:
             kubectl get pods
             kubectl get services
   
   -Note down the service's external IP and port to access the microservice.

7. Running the Client
   Prerequisites:
   Python 3.x
   Requests library (pip install requests)
   
*Usage
   Clone the client repository:
   git clone https://github.com/yourusername/microservice-client.git
   cd microservice-client

   Update the client configuration (config.py) with the microservice endpoint (local or Kubernetes):
   BASE_URL = 'http://localhost:5000'  # Update with your microservice endpoint

   Run the client application:
   python client.py


   
   
