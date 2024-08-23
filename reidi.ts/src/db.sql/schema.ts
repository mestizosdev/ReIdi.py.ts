import { text, integer, sqliteTable } from 'drizzle-orm/sqlite-core'

export const subscriptions = sqliteTable('subscriptions', {
  id: integer('id').primaryKey(),
  subscriber: text('subscriber').notNull(),
  token: text('token').notNull(),
  active: integer('active', { mode: 'boolean' }).notNull().default(true)
})

export const version = sqliteTable('version', {
  name: text('name')
})
