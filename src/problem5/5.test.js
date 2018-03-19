import { readData, writeData } from '../../utils/io'
import ultraLight from './5'

const pathIn = '/src/problem5/5.in'
const pathOut = '/src/problem5/5.out'

const inputTest = readData(`${pathIn}`).slice(1)
const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem5/5.out.nam'

describe('Problem 5', () => {
  it('should pass the sample tests', () => {
    const sample1 = '6 3 2 4'
    expect(ultraLight(sample1)).toBe(5)

    const sample2 = '6 3 1 3'
    expect(ultraLight(sample2)).toBe(1)

    const sample3 = '5 2 1 5'
    expect(ultraLight(sample3)).toBe(0)
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      const result = ultraLight(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
