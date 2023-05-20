FROM postgres:latest

ENV POSTGRES_DB mydatabase
ENV POSTGRES_USER myusername
ENV POSTGRES_PASSWORD mypassword

COPY sql/airlines.sql /docker-entrypoint-initdb.d/
COPY sql/airports.sql /docker-entrypoint-initdb.d/
COPY sql/flights.sql /docker-entrypoint-initdb.d/
COPY sql/planes.sql /docker-entrypoint-initdb.d/


EXPOSE 5432