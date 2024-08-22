import { Hono } from 'hono'
import os from 'os'
import pkg from '../../package.json'
import { version as serverVersion } from '../db/connect'

const version = new Hono()

version.get('/version', async (c) => {
  return c.json(
    {
      name: 'ReIdi',
      author: pkg.author,
      version: pkg.version,
      versionOS: os.platform() + ' ' + os.release() + ' ' + os.arch(),
      versionRuntime: `Bun ${Bun.version}`,
      versionDatabase: 'MongoDB ' + serverVersion
    },
    200
  )
})

export default version
