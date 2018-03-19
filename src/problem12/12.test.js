import { readData, writeData } from '../../utils/io'
import ultraDict from './12'

const pathIn = '/src/problem12/12.in'
const pathOut = '/src/problem12/12.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem12/12.out.nam'

describe('Problem 12', () => {
  it('should pass the sample tests', () => {
    const sample1 = '9 12 54653 370 084 156'
    expect(ultraDict(sample1)).toBe('12 156 370 54653 84 9')

    const sample2 = '1 2 3'
    expect(ultraDict(sample2)).toBe('1 2 3')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraDict(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
