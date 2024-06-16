# Basic Documentation 

## Count
```
db.entities.countDocuments()
```
## Find duplicates
```
db.entities.aggregate([ { $group: { _id: { identification: '$identification' }, uniqueIds: { $addToSet: '$_id' }, count: { $sum: 1 } } }, { $match: { count: { $gt: 1 } } }] )
```