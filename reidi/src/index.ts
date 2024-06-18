import { Hono } from 'hono'
import { poweredBy } from 'hono/powered-by'
import { logger } from 'hono/logger'

import ping from './ping/ping'
import entity from './entity/entity'
import version from './version/version'
import dbConnect from './db/connect'

const app = new Hono()

app.use(poweredBy())
app.use(logger())

if (process.env.MODE_ENV === 'development') {
  console.log('MODE ENV', process.env.MODE_ENV)
  app.route('/', version)
}

app.route('/', ping)
app.route('/', entity)

dbConnect()
  .then(() => {
    console.log('Server ready!!!')
  })
  .catch((err) => {
    console.log(`Error server ${err}`)
  })

app.onError((err, c) => {
  console.log(`Error server ${err.message}`)
  return c.json({ error: 'Internal error' }, 500)
})

export default app
