import { Hono } from 'hono'

const ping = new Hono()

ping.get('/ping', (c) => c.json({ message: 'pong' }))

export default ping
