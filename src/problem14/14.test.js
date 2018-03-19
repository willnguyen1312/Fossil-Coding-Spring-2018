import { readData, writeData } from '../../utils/io'
import ultraNum from './14'

const pathIn = '/src/problem14/14.in'
const pathOut = '/src/problem14/14.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem14/14.out.nam'

describe('Problem 14', () => {
  it('should pass the sample tests', () => {
    const sample1 = '998'
    expect(ultraNum(sample1)).toBe(8)
    const sample2 = '999999999955'
    expect(ultraNum(sample2)).toBe(1)
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraNum(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
