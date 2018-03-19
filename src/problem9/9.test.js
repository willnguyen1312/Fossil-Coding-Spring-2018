import { readData, writeData } from '../../utils/io'
import ultraRemove from './9'

const pathIn = '/src/problem9/9.in'
const pathOut = '/src/problem9/9.out'

const inputTest = readData(`${pathIn}`).slice(1)

const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem9/9.out.nam'

describe('Problem 9', () => {
  it('should pass the sample tests', () => {
    const sample1 = '1 6 9 2 4 2 1 7'
    expect(ultraRemove(sample1)).toBe('1 6 9 2 4 7')

    const sample2 = '3 10 9 9'
    expect(ultraRemove(sample2)).toBe('3 10 9')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraRemove(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
