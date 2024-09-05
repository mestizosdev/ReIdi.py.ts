const server = 'http://localhost:3000'

let message = document.querySelector('#message')
let pingButton = document.querySelector('#pingButton')

let queryInput = document.querySelector('#queryInput')
let queryButton = document.querySelector('#queryButton')
let labelQuery = document.querySelector('#labelQuery')

const headers = { 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3N1ZWRfYXQiOiIyMDI0LTA4LTIyVDE5OjQzOjUwLjc5M1oiLCJpc3N1ZXIiOiJpc3N1ZXIiLCJ1c2VybmFtZSI6IlBlcGUifQ.J7sr3W9CvigbAOe2lFhPDJEYm2qVqAWbFtjksJfkPMc' }

pingButton.addEventListener('click', getPingFromWebServices)
queryButton.addEventListener('click', getQueryFromWebServices)

window.addEventListener('load', (event) => {
  document.getElementById('queryInput').value = ''
})

function getPingFromWebServices() {
    const url = `${server}/ping`

    message.innerHTML = "Pinging ... "

    fetch(url).then((response) => {
        return response.json()
    }).then((data) => {
        console.log(data)
        message.innerHTML = data.message
    }).catch(function(error) {
        console.log(error)
        message.innerHTML = `Cannot connect to server ${url}`
    })
}

function getQueryFromWebServices() {
    const indentification = queryInput.value
    const url = `${server}/entity/${indentification}`

    labelQuery.innerHTML = "Querying ... "

    fetch(url, { headers }).then((response) => {
        return response.json()
    }).then((data) => {
        console.log(data)
        labelQuery.innerHTML = data.name
    }).catch(function(error) {
        console.log(error)
        labelQuery.innerHTML = `Cannot connect to server ${url}`
    })
}