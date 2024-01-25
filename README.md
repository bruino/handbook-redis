# Redis

Redis is an open-source, in-memory database used for storing data structures in memory, caching, and messaging.

### Concepts and Basic Commands

#### Key-Value Storage:
Redis is a key-value storage system, meaning it stores data associated with a unique key.
To store a value, you can use the SET command:
```sql
SET clave valor
```

#### Data types:
Redis supports various data types, including strings, lists, sets, hashes, etc.
Some basic commands to manipulate these data types include `GET`, `LPUSH`, `SADD`, `HSET`, etc.

##### List:
You can use lists in Redis to store an ordered sequence of elements. To add elements to a list, use `LPUSH` or `RPUSH`.
```sql
LPUSH clave valor
```

##### Sets:
Sets in Redis are unordered collections of unique elements. You can add elements to a set using `SADD`.
```sql
SADD clave elemento
```

##### Hashes:
Hashes in Redis are key-value maps. You can use them to represent more complex objects or data structures.
```sql
HSET clave campo valor
```

#### Key Expiration:
You can set a key to expire after a certain time using the `EXPIRE` command.
```sql
EXPIRE clave tiempo_en_segundos
```

##### Examples

- Strings:
```sql
SET nombre "Juan"
GET nombre
```

- Listas:
```sql
LPUSH frutas "manzana"
LPUSH frutas "naranja"
LRANGE frutas 0 -1
```

- Conjuntos:
```sql
SADD colores "rojo"
SADD colores "verde"
SADD colores "azul"
SMEMBERS colores
```

- Hashes:
```sql
HSET usuario:id123 nombre "Ana"
HSET usuario:id123 edad 25
HGETALL usuario:id123
```

- Sorted Sets:
```sql
ZADD estudiantes 90 "Carlos"
ZADD estudiantes 85 "Luis"
ZRANGE estudiantes 0 -1 WITHSCORES
```

### Data Persistence:
Redis is known for being an in-memory database, but it can also persist data to disk if necessary. You can configure persistence according to your needs.
More information [here](https://redis.io/docs/management/persistence/).


ℹ️ [Oficial Docs of Redis](https://redis.io/docs/get-started/data-store/)

### RedisTimeSeries
It is a module that extends Redis to provide specific functionalities for time series data.
    
### Creating a Time Series:
To create a time series:
```sql
TS.CREATE sensor_temperatura
```

### Inserting Data:
Add data points to the time series using `TS.ADD`. Each data point has a value and a timestamp.
```sql
TS.ADD sensor_temperatura 1548149181 25.5
TS.ADD sensor_temperatura 1548149241 26.0
```

### Querying Data:
You can retrieve data from the time series using commands like `TS.RANGE` to get a range of data points.
```sql
TS.RANGE sensor_temperatura 1548149000 1548149300
```

### Aggregations:
RedisTimeSeries supports aggregations to summarize data in specific time intervals using `TS.RANGE`.
```sql
TS.RANGE sensor_temperatura 1548149000 1548150000 AGGREGATION avg 10

```

### Reducing Resolution:
You can reduce the resolution of a time series using `TS.REDUCE` to group data points.
```sql
TS.REDUCE sensor_temperatura MAX 10
```

### Labels:
You can add labels to time series to organize and tag your data:
```sql
TS.ALTER sensor_temperatura LABELS sensor "sala"
```

### Retention Policy Configuration:
You can set a retention policy to limit the amount of data stored in the time series.
```sql
TS.CREATE sensor_temperatura RETENTION 3600
```

Official documentation for [RedisTimeSeries](https://redis.io/docs/data-types/timeseries/).


## Exmaple Project - Temperature/Humidity Sensor
n this repository, there is a script that generates random humidity and temperature values stored in Redis every second.

To start the project:
```bash
docker-compose up -d
```
The data will be persisted, and you can access it in the root of the repository in the data.ignore/ folder.

You can access the Redis client and execute the corresponding queries for this data:
```bash
% docker exec -it redis-db /bin/bash
root@c2e364f48c2c:/# redis-cli
127.0.0.1:6379> TS.GET sensor_data_channel
```

We use the official Docker image `redis/redis-stack-server`, which includes all the extra modules (in this case, the Time Series module) out of the box, allowing us to use it with zero configurations.