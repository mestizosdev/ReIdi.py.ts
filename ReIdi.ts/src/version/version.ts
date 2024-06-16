import { Hono } from 'hono'
import os from 'os'
import mongoose from '../database/db.setup'
import pkg from '../../package.json'

const version = new Hono()

const db = mongoose.connection.db

async function getMongoVersion(db: mongoose.mongo.Db) {
  const admin = db.admin()
  const serverInfo = await admin.serverInfo();

  return serverInfo.version
}


version.get('/version', async (c) => {
  const v = await getMongoVersion(db)

  return c.json({
    name: 'ReIdi.ts',
    author: pkg.author,
    version: pkg.version,
    versionOS: os.platform() + ' ' + os.release() + ' ' + os.arch(),
    versionRuntime: `Bun ${Bun.version}`,
    versionDatabase: 'Mongo ' + v
  }, 201)
}
)

export default version
