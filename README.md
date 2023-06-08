# ETL pipeline app
This README provides instructions for running the ETL process. The application allows to read the CSV files, extract the data, transform it as needed, and load it into the database.

## Installation

1. Clone the repository:
`git clone https://github.com/katarzynaamb/etl_pipeline.git`

2. Change into the project directory:
`cd etl_pipeline`

3. Ensure that the CSV files (`users.csv`, `user_experiments.csv`, `compounds.csv`) are present in the `data` directory.

4. Ensure all the scripts can be executed:
`chmod +x scripts/*.sh`

5. Ensure the Docker is installed on your machine.

## Building and running the app
Use the following command to start a script to build and run the application:

`./scripts/build_and_run.sh`

Starting the script will build (or pull)
the necessary docker images as well as start the application and database containers.

## Triggering ETL process
The `trigger_etl.sh` script performs the request to the API endpoint allowing the ETL process to start.
The script can be run using:

`./scripts/trigger_etl.sh`

## Accessing the results
After running the ETL process, you can verify that the data has been populated in the database. 
Example queries can be performed by running the `get_results.sh` script:

`./scripts/get_results.sh`

You can run any additional queries by editing the `scripts/query.sql` file accordingly.