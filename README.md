
REST API for EBI Genes Database
===============================

Api Endpoints
-------------

- http://localhost/genes?lookup=brc
- http://localhost/genes?lookup=brc&species=homosapiens

Initialization
--------------

1. Get the code::
    
        $ git clone https://github.com/dteklavya/ebi-flask-app.git

        $ cd ebi-flask-app

    
    Service can be started in development mode or can be deployed using docker.

2. Deploy using Docker::

       $ docker run --env-file .env -p 80:5000 kanakraj/ebi-genes-api:v0
  
3. Run the Flask development server::

      
        $ python -m venv venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt
        $ ./start.sh
The API will be accesible on port 5000 http://localhost:5000/

Testing
-------

Unit tests for the application are included in the code base and tests can be run from the codebase as::
  
        python -m unittest

It is advisable to use Docker Hub or another CI/CD pipeline to automatically build and tag a Docker image and test it.

Deployment
----------

Docker container can be deployed manually using commands listed above. Or container orchetration/clustering tools can be used to deploy and manage it.

The solution has been implemented keeping following points in mind to ensure better scaling without significant changes to tooling or development practices:

- Dependency: All dependencies are explicitly declared and isolated using virtual environment for Python.
- Configuration: Information such as database credentials and other values are retrived from environment so that these can be changed without changing the code. The .env file in repository has been added knowingly but it can be easily replaced with any config file while running the cotainer.
- Seperate build and run processes.
- Both error and access logs (of Gunicorn application server) are directed to STDOUT for centralized storage and retrieval.
        - The app exports HTTP as a service by binding to a port (using Gunicorn), and listening to requests coming in on that port.


Documentation
-------------

Python code has been appropriately commented using Docstrings for Classes, modules, methods, functions etc. Docstrings can be used in conjunction with document generation tools to auto generate feature rich documentation for codebase.

It is advisable for the project to have space for documentation and must contain atleast following sections:

- Tutorials: Simple steps that take the reader through to complete a project. Useful for onboarding new developers.
- How-To: Guides that take the reader through the steps required to get s job done or solve a problem. Example, "How to Contribute".
- References: Linkes to external and internal resources.
- Explanations: Technical descriptions of the software and how to use it (Classes, functions, APIs, etc.). This is where Python Docstrings play crucial role as module, Class, method specific documentation can be auto generated with code in HTML rich style.

