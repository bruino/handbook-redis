# Redis

Redis es una base de datos en memoria open source que se utiliza para almacenar estructuras de datos en memoria, caché y mensajería.

### Conceptos y comandos básicos

#### Almacenamiento clave-valor:
Redis es un sistema de almacenamiento clave-valor, lo que significa que almacena datos asociados con una clave única.
Para almacenar un valor, puedes usar el comando SET:
```sql
SET clave valor
```

#### Tipos de datos:
Redis admite varios tipos de datos, incluyendo: strings, listas, conjuntos, hashes, etc.
Algunos comandos básicos para manipular estos tipos de datos: GET, LPUSH, SADD, HSET, etc.

##### Listas:
Puedes utilizar listas en Redis para almacenar una secuencia ordenada de elementos. Para agregar elementos a una lista, usando `LPUSH` o `RPUSH`.
```sql
LPUSH clave valor
```

##### Conjuntos:
Los conjuntos en Redis son colecciones no ordenadas de elementos únicos. Puedes agregar elementos a un conjunto utilizando SADD.
```sql
SADD clave elemento
```

##### Hashes:
Los hashes en Redis son mapas clave-valor. Puedes usarlos para representar objetos o estructuras de datos más complejas.
```sql
HSET clave campo valor
```

#### Expiración de claves:
Puedes configurar una clave para que expire después de cierto tiempo con el comando EXPIRE.
```sql
EXPIRE clave tiempo_en_segundos
```

##### Ejemplos

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

### Persistencia de datos:
Redis es conocido por ser una base de datos en memoria, pero también puede persistir datos en disco si es necesario. Puedes configurar la persistencia según tus necesidades.
Mas informacion [aqui](https://redis.io/docs/management/persistence/).


ℹ️ [Documentación oficial de Redis](https://redis.io/docs/get-started/data-store/)

### RedisTimeSeries
Es un módulo que extiende Redis para ofrecer funcionalidades específicas para series temporales.

Informacion de la instalacion aqui.
    
### Creación de una serie temporal:
Para crear una serie temporal:
```sql
TS.CREATE sensor_temperatura
```

### Inserción de datos:
Añade puntos de datos a la serie temporal utilizando `TS.ADD``. Cada punto de datos tiene un valor y una marca de tiempo.
```sql
TS.ADD sensor_temperatura 1548149181 25.5
TS.ADD sensor_temperatura 1548149241 26.0
```

### Consulta de datos:
Puedes recuperar datos de la serie temporal utilizando comandos como TS.RANGE para obtener un rango de puntos de datos.
```sql
TS.RANGE sensor_temperatura 1548149000 1548149300
```

### Agregaciones:
RedisTimeSeries admite agregaciones para resumir datos en intervalos de tiempo específicos usando `TS.RANGE`
```sql
TS.RANGE sensor_temperatura 1548149000 1548150000 AGGREGATION avg 10

```

### Reducción de la resolución:
Puedes reducir la resolución de una serie temporal usando `TS.REDUCE` para agrupar puntos de datos.

```sql
TS.REDUCE sensor_temperatura MAX 10
```

### Labels:
Puedes agregar etiquetas a las series temporales para organizar y etiquetar tus datos:
```sql
TS.ALTER sensor_temperatura LABELS sensor "sala"
```

### Configuración de retención:
Se puede establecer una política de retención para limitar la cantidad de datos almacenados en la serie temporal.

```sql
TS.CREATE sensor_temperatura RETENTION 3600
```

Documentación oficial de RedisTimeSeries.


## Proyecto - Sensor de Temperatura/Humedad

En el presente repo hay un script generador de valores aleatorios de humedad y temperatura que se almacenan en Redis cada segundo.

Para iniciar el proyecto:
```bash
docker-compose up -d
```

Los datos seran persistidos y podras accederlos en la raiz del repositorio en la carpeta `data.ignore/`.