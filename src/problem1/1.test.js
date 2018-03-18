import { readData, writeData } from '../../utils/io'
import ultraTrim from './1'

const pathIn = '/src/problem1/1.in'
const pathOut = '/src/problem1/1.out'

const inputTest = readData(`${pathIn}`)
const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem1/1.out.nam'

describe('Problem 1', () => {
  it('should pass the tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      const result = ultraTrim(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
