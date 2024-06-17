import { Hono } from 'hono'
import personModel from '../db/persons.model'

const entity = new Hono()

entity.get('/entity/:identification', async (c) => {
  const identification = c.req.param('identification')

  const person = await personModel.findOne({ identification })

  if (!person) {
    return c.json('Not found', 404)
  }

  return c.json(person.toObject())
})

export default entity
