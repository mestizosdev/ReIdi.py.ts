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
## Search to extract for the persons collection
```
db.taxpayers.find({type:'PERSONAS NATURALES'}).projection({_id:0,'ruc':'$identification',identification:{$substr: [ "$identification", 0, 10 ]},name:1,province:1,canton:1,parish:1})
```