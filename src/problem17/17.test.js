import { readData, writeData } from '../../utils/io'
import ultraFibo from './17'

const pathIn = '/src/problem17/17.in'
const pathOut = '/src/problem17/17.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

inputTest.pop()

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem17/17.out.nam'

describe('Problem 17', () => {
  it('should pass the sample tests', () => {
    const sample1 = '55 21 34 5 6 144 610'
    expect(ultraFibo(sample1)).toBe('8 13 89 233 377')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraFibo(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
