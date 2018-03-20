import { readData, writeData } from '../../utils/io'
import ultraLocal from './16'

const pathIn = '/src/problem16/16.in'
const pathOut = '/src/problem16/16.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

inputTest.pop()

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem16/16.out.nam'

describe('Problem 16', () => {
  it('should pass the sample tests', () => {
    const sample1 = '15 30 10 19'
    expect(ultraLocal(sample1)).toBe('1 2')

    const sample2 = '31 15 27 31 32 32 31 9 4 21'
    expect(ultraLocal(sample2)).toBe('1 8')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraLocal(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
