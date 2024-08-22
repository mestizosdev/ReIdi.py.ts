import mongoose from 'mongoose'

let version: string
const mongoUri = process.env.MONGODB_URI || 'mongodb://localhost:27017/ecuador'

export default async function dbConnect() {
  const db = await mongoose.connect(String(mongoUri))

  const admin = db.connection.db.admin()
  const serverInfo = await admin.serverInfo()
  version = serverInfo.version
  console.log('MongoDB connected', version)
}

export { version }
