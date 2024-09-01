# MongoDB
## Querys

### ilike
```
db.taxpayers.find({ "name": { $regex: /banco central/i } });
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