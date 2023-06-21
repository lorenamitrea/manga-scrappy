# manga-scrappy

1. update requirements.txt file if it is needed
2. install/start docker desktop
3. run `docker-compose build` command to build the containers for the apps
4. run `docker-compose up` command to start the containers

how to connect to db from container 
- psql -U postgres
- \l list databases
- \c <dbname> connect to <dbname> database
- \dt describe tables in database
- 