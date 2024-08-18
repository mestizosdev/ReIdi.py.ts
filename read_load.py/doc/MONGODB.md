# Basic Documentation 
## Basic commands
### Start mongo shell
```
mongosh
```
### Show databases
```
show databases
```
### Use database
```
use ecuador     
```
## Count
```
db.taxpayers.countDocuments()
```
## Group
```
db.taxpayers.aggregate([ { $group: { _id: '$type', count: { $sum: 1 } } }] )
```
## Find ilike
```
db.taxpayers.find({name: /.*jorge luis.*/i})
```
## Find not in
```
db.taxpayers.find({type:{$nin:['PERSONAS NATURALES']}})
```
## Find duplicates
```
db.taxpayers.aggregate([ { $group: { _id: { identification: '$identification' }, uniqueIds: { $addToSet: '$_id' }, count: { $sum: 1 } } }, { $match: { count: { $gt: 1 } } }] )
```
## Search to extract for the persons collection
```
db.taxpayers.find({type:'PERSONAS NATURALES'}).projection({_id:0,'ruc':'$identification',identification:{$substr: [ "$identification", 0, 10 ]},name:1,province:1,canton:1,parish:1})
```
