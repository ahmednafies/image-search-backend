# Image Search Backend

## Setup

Go to the GCP console and download the credentials for the hackathon-product-detection service account.
Save the JSON somewhere and set the `GOOGLE_APPLICATION_CREDENTIALS` to point to the JSON. For example:

```
  $ export GOOGLE_APPLICATION_CREDENTIALS=$PWD/fyndiq-4f8d604db4da.json
```

TODO: This should be picked up by the docker-compose, can be solved by agreeing on a folder to place that file
and pick it by using a volume

## Run

```bash
  $ make run
```

API docs can be found at `http://localhost:8000/docs`
