import { Hono } from 'hono'
import { z } from 'zod'

import personModel from '../db/person.model'
import taxpayerModel from '../db/taxpayer.model'

const entity = new Hono()
const stringLenght10or13 = z
  .string()
  .refine(
    (val) => (val.length === 10 || val.length === 13) && /^\d+$/.test(val),
    {
      message:
        'String must be either 10 or 13 characters long and contains only numbers'
    }
  )

entity.get('/entity/:identification', async (c) => {
  const identification = c.req.param('identification')

  const result = stringLenght10or13.safeParse(identification)

  if (!result.success) {
    return c.json(result.error.errors, 404)
  }

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
