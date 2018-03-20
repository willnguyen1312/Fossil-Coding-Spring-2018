import { readData, writeData } from '../../utils/io'
import ultraRotate from './18'

const pathIn = '/src/problem18/18.in'
const pathOut = '/src/problem18/18.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

inputTest.pop()

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem18/18.out.nam'

describe('Problem 18', () => {
  it('should pass the sample tests', () => {
    const sample1 = '1 abc'
    expect(ultraRotate(sample1)).toBe('bcd')

    const sample2 = '2 9zb'
    expect(ultraRotate(sample2)).toBe('b1d')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraRotate(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
