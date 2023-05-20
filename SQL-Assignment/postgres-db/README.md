### Download the Docker Image, Build it locally and create a container

1. `docker pull postgres`

2. `docker build -t my-postgres-image .`

3. `docker run -d -p 5432:5432 --name my-postgres-container my-postgres-image`


### Check if the table can be queried

1. Open your terminal and run the following command 

    `docker exec -it my-postgres-container bash`

2. Run the following command to connect to the Postgres database:

    `psql -U myusername -d mydatabase`

3. Run the following command to list all the tables in the database:

    `\dt`

4. To view the contents of a specific table, you can run the following command:

    `SELECT * FROM public.airlines;`

### Connect to your favourite SQL IDE and write the queries for questions

