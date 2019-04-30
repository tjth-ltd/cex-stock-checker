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
* Update working/check-cex-stock.py with your Product ID
* Execute the script:

```
sudo docker exec -it cex-stock-checker python /working/check-cex-stock.py
```

# Future features:

* Web interface for entering URL for requests
* Parsing full URL for Product ID
* Email notification when in stock
* Instructions for Scheduling in Cron
* Json reading for multiple checks