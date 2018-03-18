const { readdirSync } = require('fs-extra')

// eslint-disable-next-line
const arr_dirs = readdirSync('./src')
console.log(arr_dirs)
