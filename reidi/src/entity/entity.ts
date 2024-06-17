import { Hono } from 'hono'
import personModel from '../db/person.model'
import taxpayerModel from '../db/taxpayer.model'

const entity = new Hono()

entity.get('/entity/:identification', async (c) => {
  const identification = c.req.param('identification')

  if (identification.length === 10) {
    const person = await personModel.findOne({ identification })

    if (!person) {
      return c.json('Not found', 404)
    }

    return c.json(person.toObject())
  } else if (identification.length === 13) {
    const taxpayer = await taxpayerModel.findOne({ identification })

    if (!taxpayer) {
      return c.json('Not found', 404)
    }

    return c.json(taxpayer.toObject())
  }

  return c.json('Not found', 404)
})

export default entity
