import { readData, writeData } from '../../utils/io'
import ultraShorten from './19'

const pathIn = '/src/problem19/19.in'
const pathOut = '/src/problem19/19.out'

const inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

inputTest.pop()

const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem19/19.out.nam'

describe('Problem 19', () => {
  it('should pass the sample tests', () => {
    const sample1 = 'baabc'
    expect(ultraShorten(sample1)).toBe('c')

    const sample2 = 'abc'
    expect(ultraShorten(sample2)).toBe('abc')

    const sample3 = 'aa'
    expect(ultraShorten(sample3)).toBe('Empty String')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraShorten(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
