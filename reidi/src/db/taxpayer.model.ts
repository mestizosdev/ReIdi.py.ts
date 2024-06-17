import { Schema, model } from 'mongoose'

export interface ITaxpayerSchema {
  identification: string
  name: string
}

const taxpayerSchema = new Schema<ITaxpayerSchema>({
  identification: {
    type: String,
    required: true
  },
  name: {
    type: String,
    required: true
  }
})

const taxpayerModel = model('taxpayers', taxpayerSchema)

export default taxpayerModel
