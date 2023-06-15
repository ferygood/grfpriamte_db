# TFprimate_db
PostgreSQL database for TFprimate

```sql
#import csv file in table primategrfs
 \COPY primategrfs FROM './raw_data/23GRFs_ortholog_transcripts_for_database.csv' delimiter ',' CSV HEADER;
```

## restore `tfprimate.sql` to `tfprimate` table
```shell
# restore
psql -U postgres -W -d tfprimate -f tfprimate.sql

# login
psql -U postgres -d tfprimate
```


# Table Schema ERD
![ERD Diagram](ERD_05252023.png)

## Containerize
```shell
# 1 get postgresql image
docker pull postgres

# 2 build docker image
docker build -t <image-name> .

# 3 run container
docker run --name <container-name> -p 5432:5432 -d <image-name>

# execute example
docker exec -it <container-name> /bin/bash
```

## FastAPI
- Interactive API docs can be access `/docs`
- Alternative API docs `/redoc` 
```shell
uvicorn main:app --reload
```