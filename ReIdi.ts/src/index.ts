import { Hono } from 'hono'
import ping from './ping/ping'
import version from './version/version'

const app = new Hono()

app.route('/', ping)
app.route('/', version)

export default app
