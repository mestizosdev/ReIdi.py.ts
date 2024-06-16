# Basic Documentation 

## Count
```
db.entities.countDocuments()
```
## Group
```
db.entities.aggregate([ { $group: { _id: '$type', count: { $sum: 1 } } }] )
```
## Find
```
db.entities.find({name: /.*jorge luis.*/i})
```
## Find duplicates
```
db.entities.aggregate([ { $group: { _id: { identification: '$identification' }, uniqueIds: { $addToSet: '$_id' }, count: { $sum: 1 } } }, { $match: { count: { $gt: 1 } } }] )
```
