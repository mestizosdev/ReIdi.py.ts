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
## Remote connection
### Add IP server
Edit file /etc/mongod.conf and add the following IP:
```
# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1, mongodb_server_ip
```
and restart mongod
```
sudo systemctl restart mongod
```
### Test
```
nc -zv mongodb_server_ip 27017
```