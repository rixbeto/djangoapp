For Run and test this application do you need docker installed

If you nned some help to install it -> https://docs.docker.com/engine/install/

Once you have docker installed, maybe you want to follow next steps:

Position in the root directory of the project --> app

Run command to build the docker image ->
    docker build -t djangoapp .

Once you have the image created you can run the docker compose  container commands to set-up full environment:
    docker-compose up

Your app ready to use, test time!, 

In your browser

url: http://localhost:8000

#------ You need to setup your app with next steeps: 

    1. Run your commands to create and up your docker containers
        i. docker build -t djangoapp .
        ii. docker-compose up --build
    2. Go to url: http://localhost:8080
        i. Using parameters to connect to postgresql database;
            user: postres
            password: example
            Create database named -> learning 
        iii. Go to the djangoapp container to run commands: 

            docker exec -it djangoapp bash <---- to connect to the container

            To create tables: 
            ./manage.py makemigrations
            ./manage.py migrate 
            ./manage.py createsuperuser  <---- and follow the prompt instructions

    3. Fill dtabase with some parameters: 

        To create some items --->  http://localhost:8000/createproducts
        To change price from current items ---> http://localhost:8000/change_price
        To set some products to the user using postman and json body
        {
            "products":[1,12,14,13],
            "user_id":1
        }

        To mark as seen  notification --> http://localhost:8000/watched/1
