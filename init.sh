#!/usr/bin/env bash

# Setup DB Connection String
AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN

AIRFLOW__WEBSERVER__SECRET_KEY="openssl rand -hex 30"
export AIRFLOW__WEBSERVER__SECRET_KEY

DBT_POSTGRESQL_CONN="postgresql+psycopg2://${DBT_POSTGRES_USER}:${DBT_POSTGRES_PASSWORD}@${DBT_POSTGRES_HOST}:${POSTGRES_PORT}/${DBT_POSTGRES_DB}"


cd /dbt && dbt compile
rm -f /airflow/airflow-webserver.pid

airflow users  create --role Admin --username admin --email danielzelalemheru@gmail.com --firstname admin --lastname admin --password admin

sleep 10
airflow db upgrade
sleep 10


airflow connections add 'mysql_conn_id'  --conn-uri "mysql+mysqldb://${DBT_MYSQL_USER}:${DBT_MYSQL_PASSWORD}@${DBT_MYSQL_HOST}:${MYSQL_PORT}/${DBT_MYSQL_DB}"
airflow connections add 'postgres_conn_id' --conn-uri $DBT_POSTGRESQL_CONN

airflow scheduler & airflow webserver