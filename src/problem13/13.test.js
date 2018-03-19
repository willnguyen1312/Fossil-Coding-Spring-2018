import { readData, writeData } from '../../utils/io'
import ultraMatrix from './13'

const pathIn = '/src/problem13/13.in'
const pathOut = '/src/problem13/13.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem13/13.out.nam'

describe('Problem 13', () => {
  it('should pass the real tests', () => {
    const output = []
    let indexInput = 0
    let indexOutput = 0
    while (inputTest[indexInput]) {
      const expected = outputTest[indexOutput]
      const input = inputTest
        .slice(indexInput + 1, indexInput + 1 + +inputTest[indexInput])
        .map(x => x.split(' '))

      const result = ultraMatrix(input)

      expect(result).toBe(expected)
      output.push(result)
      indexOutput += 1
      indexInput = indexInput + 1 + +inputTest[indexInput]
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
