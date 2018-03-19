import { readData, writeData } from '../../utils/io'
import ultraCoords from './15'

const pathIn = '/src/problem15/15.in'
const pathOut = '/src/problem15/15.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem15/15.out.nam'

describe('Problem 15', () => {
  it('should pass the sample tests', () => {
    const sample1 = '0 0 1 1 0 -1 1 0'
    expect(ultraCoords(sample1)).toBe('YES')
    const sample2 = '1 2 3 4 12 32 87 25'
    expect(ultraCoords(sample2)).toBe('NO')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraCoords(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
