import mongoose from 'mongoose'

let version: string
export default async function dbConnect() {
  const db = await mongoose.connect(String(process.env.MONGODB_URI))

  const admin = db.connection.db.admin()
  const serverInfo = await admin.serverInfo()
  version = serverInfo.version
  console.log('MongoDB connected', version)
}

export { version }
