import { Schema, model } from 'mongoose'

export interface IPersonSchema {
    identification: string
    name: string
}

const personSchema = new Schema<IPersonSchema>({
    identification: {
        type: String,
        required: true
    },
    name: {
        type: String,
        required: true
    }
})

const personModel = model('persons', personSchema)

export default personModel