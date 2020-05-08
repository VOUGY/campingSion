# Mandatory

Please, first, follow [this documentation](https://docs.djangoproject.com/fr/3.0/ref/contrib/gis/install/) to install
geodjango.

Finaly, you can configurate a postgis server or use a postgis container as follow:
```bash
docker run --name=postgis -d \
-e POSTGRES_USER=alex \
-e POSTGRES_PASS=password \ 
-e POSTGRES_DBNAME=gis \
-e ALLOW_IP_RANGE=0.0.0.0/0 \
-p 25432:5432 \
-v pg_data:/var/lib/postgresql kartoza/postgis:12.0
```

# Docker help

```
docker ps                # Display running containers
docker ps -all           # Display all containers
docker rm <container_id> # Delete a container
docker images ls         # List all local images
docker rmi <image_id>    # Delete a image
```

# Run the project

This documentation, takes into account that you have already created a virtualenv for this project.

1. Copy `.env.example` to `.env`
2. Adapt `.env`
3. Install libs `pip install -r requirements.txt`
4. Apply django migration `python manage.py migrate`
5. Populate DB `python manage.py loaddata */fixtures/*.json`
6. Start server `python manage.py runserver`
