import { Hono } from 'hono'
import { poweredBy } from 'hono/powered-by'
import { logger } from 'hono/logger'

import ping from './ping/ping'
import entity from './entity/entity'
import version from './version/version'
import dbConnect from './db/connect'
import personModel from './db/persons.model'

const app = new Hono()

app.use(poweredBy())
app.use(logger())

app.route('/', ping)
app.route('/', entity)
app.route('/', version)

dbConnect()
  .then(() => {
    app.get('/', async (c) => {
      const persons = await personModel.find({ identification: '0400882965' })

      return c.json(
        persons.map((p) => p.toObject()),
        200
      )
    })

    app.get('/:identification', async (c) => {
      const identification = c.req.param('identification')

      const person = await personModel.findOne({ identification })

      if (!person) {
        return c.json('Not found', 404)
      }

      return c.json(person.toObject())
    })
  })
  .catch((err) => {
    app.get('/*', (c) => {
      return c.text(`Failed to connect to database: ${err.message}`)
    })
  })

app.onError((err, c) => {
  return c.text(`App Error: ${err.message}`)
})

export default app
