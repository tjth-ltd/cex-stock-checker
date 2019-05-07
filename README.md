# CEX Stock Checker

A Python based (Run within docker-compose) CEX Stock checker

## Installation

To install this package - Clone the repository to your Docker host and build the container:

```
cd cex-stock-checker
docker-compose up -d
```

## Usage

* Get the Product ID from the URL of the Product
* Update working/check-cex-stock.py with your Product ID (Multiple productIDs can be used, comma separated)
* Update sendmail.py with your SMTP Credentials (Eg Gmail, Mailgun etc)
* Execute the script by running the below command (Note, the first run will install the latest version of pyppeter Chromium):

```
sudo docker exec -it cex-stock-checker python /working/check-cex-stock.py
```

## Scheduling to run in Cron

* To run this script on a schedule in Cron, add an entry as below to /etc/crontab. the example below will run every 5 minutes.

```
*/5 * * * * root docker exec cex-stock-checker python /working/check-cex-stock.py
```

# Future features:

* Web interface for submitting URL for requests
* Parsing full URL for Product ID
* Using Docker provided environment variables for SMTP Details