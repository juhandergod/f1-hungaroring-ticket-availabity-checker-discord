# F1 Hungaroring - ticket availability checker bot for Discord

--------
## About 

The project was created to get notification to any platform, when there is available weekend ticket for F1 Hungaroring GP.
For this case I chose Discord channel notification.

---------
## Usage

### Running with Docker

Building the docker image from source locally:
```
docker build -t f1-hungaroring-ticket-checker .
```

*You should be in the sources folder where the Dockerfile is located to run this script.*

Running the local docker-image:
Instead of having `$WEBHOOK_URL` give your discord's channel url link.
```
docker run --name f1-hungaroring-ticket-checker -it -d --env WEBHOOK_URL=$WEBHOOK_URL f1-hungaroring-ticket-checker
```


------
## Contributors

Created by @juhanderpro.
