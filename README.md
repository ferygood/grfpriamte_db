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