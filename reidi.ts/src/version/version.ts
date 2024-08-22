import { Hono } from 'hono'
import { platform, release, arch } from 'os'
import pkg from '../../package.json'
import { version as serverVersion } from '../db/connect'

const version = new Hono()

version.get('/version', async (c) => {
  return c.json(
    {
      name: 'ReIdi',
      author: pkg.author,
      version: pkg.version,
      versionOS: platform() + ' ' + release() + ' ' + arch(),
      versionRuntime: `Bun ${Bun.version}`,
      versionNoSqlDatabase: 'MongoDB ' + serverVersion
    },
    200
  )
})

export default version
