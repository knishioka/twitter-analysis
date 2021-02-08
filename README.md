# twitter-analysis
## Quick Start

### Build image

```bash
docker build -t twitter-analysis .
```

### Set env

```bash
cp .env.sample .env
vi .env
```

### Run bash on container

```bash
docker run --rm --env-file=.env -it -v $(pwd):/usr/src/app twitter-analysis bash
```
