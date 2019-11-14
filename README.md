# REST API for EBI Genes Database

## Api Endpoints

- http://localhost/genes?lookup=brc
- http://localhost/genes?lookup=brc&species=homosapiens

## Initialization

    Service can be started in development mode or can be deployed using docker.

    - Deploy using Docker
      - $ docker run -p 80:5000 kanakraj/ebi-genes-api
  
    - Development
      - After cloning the git repository:
        - $ python -m venv venv
        - $ source venv/bin/activate
        - $ pip install -r requirements.txt
      - Start the Flask development server
        - ./start.sh
        - The API will be accesible on port 5000 http://localhost:5000/

## Deployment

    Docker container can be deployed manually using commands listed above. Or container orchetration/clustering tools can be used to deploy and manage it.

    The solution has been implemented keeping following points in mind to ensure better scaling without significant changes to tooling or development practices:

        - Dependency: All dependencies are explicitly declared and isolated.
        - Configuration: Information such as credentials and other resources are retrived from environment so that these can be changed without changing the code.
        - 