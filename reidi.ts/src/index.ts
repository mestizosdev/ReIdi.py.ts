import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { poweredBy } from 'hono/powered-by'

import log from './logger'
import ping from './ping/ping'
import entity from './entity/entity'
import version from './version/version'
import dbConnect from './db.nosql/connect'

const app = new Hono()

app.use(poweredBy())
app.use('/*', cors())

if (process.env.MODE_ENV === 'development') {
  log.info(`Startup in ${process.env.MODE_ENV} mode`)
  app.route('/', version)
}

app.route('/', ping)
app.route('/', entity)

dbConnect()
  .then(() => {
    log.info('Server ready!!!')
  })
  .catch((err) => {
    log.error(`Error server ${err}`)
  })

export default app
