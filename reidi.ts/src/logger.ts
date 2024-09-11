import { createLogger, format, transports } from 'winston'
const { combine, timestamp, colorize } = format

// Custom format for console logging with colors
const consoleLogFormat = combine(
  colorize(),
  format.printf(({ level, message }) => {
    return `${level}: ${message}`
  })
)

// Create a Winston logger
const log = createLogger({
  level: 'info',
  format: combine(
    timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    format.align(),
    format.printf(
      (info) => `${info.level}: ${[info.timestamp]}: ${info.message}`
    )
  ),
  transports: [
    new transports.Console({
      format: consoleLogFormat
    }),
    new transports.File({ filename: 'server.log' })
  ]
})

export default log
