# Querys

## ilike
```
db.taxpayers.find({ "name": { $regex: /banco central/i } });
```