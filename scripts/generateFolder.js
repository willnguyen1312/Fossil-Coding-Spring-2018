const mkdirp = require('mkdirp')

const arr = Array.from({ length: 20 }, (v, i) => i + 1)

for (const num of arr) {
  mkdirp(`src/problem${num}`)
}
