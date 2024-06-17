import { Hono } from 'hono'
import os from 'os'
import pkg from '../../package.json'

const version = new Hono()

version.get('/version', async (c) => {

  return c.json(
    {
      name: 'ReIdi',
      author: pkg.author,
      version: pkg.version,
      versionOS: os.platform() + ' ' + os.release() + ' ' + os.arch(),
      versionRuntime: `Bun ${Bun.version}`,
      versionDatabase: 'Mongo '
    },
    201
  )
})

export default version
