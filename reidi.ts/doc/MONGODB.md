# MongoDB
## Querys

### ilike
```
db.taxpayers.find({ "name": { $regex: /banco central/i } });
```
## Drop Database
```
show dbs
```
```
use ecuador
```
```
db.dropDatabase()
```
## Backup and Restore
### Backup
```
mongodump --db ecuador
```
### Restore
```
mongorestore dump
```
