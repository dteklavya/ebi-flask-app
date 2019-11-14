# REST API for EBI Genes Database

## Api Endpoints

- http://localhost/genes?lookup=brc
- http://localhost/genes?lookup=brc&species=homosapiens

## Initialization

    Get the code:
    
        $ git clone https://github.com/dteklavya/ebi-flask-app.git

        $ cd ebi-flask-app

    
    Service can be started in development mode or can be deployed using docker.

    - Deploy using Docker
      - $ docker run --env-file .env -p 80:5000 kanakraj/ebi-genes-api
  
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

        - Dependency: All dependencies are explicitly declared and isolated using virtual environment for Python.
        - Configuration: Information such as database credentials and other values are retrived from environment so that these can be changed without changing the code. The .env file in repository has been added knowingly but it can be easily replaced with any config file while running the cotainer.
        - Seperate build and run processes.
        - Both error and access logs (of Gunicorn application server) are directed to STDOUT for centralized storage and retrieval.
        - The app exports HTTP as a service by binding to a port (using Gunicorn), and listening to requests coming in on that port.

## Testing

    Unit tests for the application are included in the code base.

## Documentation

    The Python code has been appropriately commented using Docstrings for Class, methods, functions etc. Docstrings can be used in conjunction with document generation tools to auto generate feature rich documentation for codebase.

    Every project must have space for documentation and must contain atleast following sections:
        1. Tutorials: Simple steps that take the reader through to complete a project.
        2. How-To: Guides that take the reader through the steps required to get s job done or solve a problem. Example, "How to Contribute".
        3. References: Linkes to external and internal resources.
        4. Explanations: Technical descriptions of the software and how to use it (Classes, functions, APIs, etc.).

