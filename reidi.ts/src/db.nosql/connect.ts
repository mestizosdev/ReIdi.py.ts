import mongoose from 'mongoose'
import log from '../logger'

let version: string
const mongoUri = process.env.MONGODB_URI || 'mongodb://localhost:27017/ecuador'

export default async function dbConnect() {
  try {
    const db = await mongoose.connect(String(mongoUri))

    const admin = db.connection.db.admin()
    const serverInfo = await admin.serverInfo()
    version = serverInfo.version
    console.log('MongoDB connected', version)
  } catch (error) {
    log.error(`Could not connect to MongoDB ${mongoUri} ${error}`)
  }
}

export { version }
