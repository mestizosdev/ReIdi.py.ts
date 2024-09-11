import { Hono } from 'hono'
import { z } from 'zod'
import { zValidator } from '@hono/zod-validator'
import { bearerAuth } from 'hono/bearer-auth'
import { eq, and } from 'drizzle-orm'

import log from '../logger'
import personModel from '../db.nosql/person.model'
import taxpayerModel from '../db.nosql/taxpayer.model'

import db from '../db.sql/connect'
import { subscriptions } from '../db.sql/schema'

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

entity.use(
  '/entity/*',
  bearerAuth({
    verifyToken: async (token) => {
      const result = await getTokenFromDb(token)
      return result
    }
  })
)

entity.get(
  '/entity/:identification',
  zValidator('param', z.object({ identification: stringLenght10or13 })),
  async (c) => {
    const identification = c.req.param('identification')

    switch (identification.length) {
      case 10: {
        const person = await personModel.findOne({ identification })
        if (person) {
          return c.json(person.toObject())
        }
        break
      }
      case 13: {
        const taxpayer = await taxpayerModel.findOne({ identification })
        if (taxpayer) {
          return c.json(taxpayer.toObject())
        }
        break
      }
    }

    return c.json('Not found', 404)
  }
)

async function getTokenFromDb(token: string): Promise<boolean> {
  const result = await db
    .select({
      subscriberField: subscriptions.subscriber
    })
    .from(subscriptions)
    .where(and(eq(subscriptions.token, token), eq(subscriptions.active, true)))

  if (!result.length) {
    return false
  }

  const { subscriberField } = result[0]
  log.info(`Subscriber ${subscriberField} request a resource`)
  return true
}

export default entity
