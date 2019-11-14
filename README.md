# REST API for EBI Genes Database

Api Endpoints

- http://localhost/genes?lookup=brc
- http://localhost/genes?lookup=brc&species=homosapiens

Initialization:

    Service can be started in development mode or can be deployed using docker.

    - Development
      - After cloning the git repository:
        - $ python -m venv venv
        - $ source venv/bin/activate
        - $ pip install -r requirements.txt
      - Start the Flask development server
        - ./start.sh
        - The API will be accesible on port 5000 http://localhost:5000/

    - Deploy using Docker
      - $ docker run -p 80:5000 kanakraj/ebi-genes-api
