import { Hono } from 'hono'
import { poweredBy } from 'hono/powered-by'
import { logger } from 'hono/logger'

import log from './logger'
import ping from './ping/ping'
import entity from './entity/entity'
import version from './version/version'
import dbConnect from './db/connect'

const app = new Hono()

app.use(poweredBy())
app.use(logger())

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

// app.onError((err, c) => {
//   log.error(`Error server ${err.message}`)
//   return c.json({ error: 'Internal error' }, 500)
// })

export default app
