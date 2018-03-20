import { readData, writeData } from '../../utils/io'
import ultraString from './20'

const pathIn = '/src/problem20/20.in'
const pathOut = '/src/problem20/20.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

inputTest.pop()

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem20/20.out.nam'

describe('Problem 20', () => {
  it('should pass the sample tests', () => {
    const sample1 = 'ABA XXABABAXX'
    expect(ultraString(sample1)).toBe(2)
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraString(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
