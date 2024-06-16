import mongoose from 'mongoose';

// Connect to the MongoDB database
const mongoDBURI = 'mongodb://localhost:27017';

mongoose.connect(mongoDBURI);
export default mongoose;