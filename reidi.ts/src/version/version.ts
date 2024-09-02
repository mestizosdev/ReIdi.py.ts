import { Hono } from 'hono'
import { platform, release, arch } from 'os'
import pkg from '../../package.json'
import { version as serverVersion } from '../db.nosql/connect'
import db from '../db.sql/connect'
import { version as sqliteVersion } from '../db.sql/schema'

const version = new Hono()

version.get('/version', async (c) => {
  const result = await db
    .select({ numberVersion: sqliteVersion.name })
    .from(sqliteVersion)
  const { numberVersion } = result[0]

  return c.json(
    {
      name: 'ReIdi',
      author: pkg.author,
      website: 'https://mestizos.dev',
      version: pkg.version,
      versionOS: platform() + ' ' + release() + ' ' + arch(),
      versionRuntime: `Bun ${Bun.version}`,
      versionNoSqlDatabase: 'MongoDB ' + serverVersion,
      versionSqlDatabase: 'SQLite ' + numberVersion
    },
    200
  )
})

export default version
