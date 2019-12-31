# Crawlab

```bash
# build
docker build -f ./Dockerfile.frontend -t bitsean/crawlab-frontend:0.1 .

# run
docker run --rm -p 5000 -e CRAWLAB_API_ADDRESS=http://172.17.3.83:31705  bitsean/crawlab-frontend:0.1
```

```bash
# build
docker build -f ./Dockerfile.backend -t bitsean/crawlab-backend:0.1 .

# run
docker run --rm -e CRAWLAB_SERVER_MASTER=N -e CRAWLAB_REDIS_ADDRESS=redis -e CRAWLAB_MONGO_HOST=mongo bitsean/crawlab-backend:0.1
```
