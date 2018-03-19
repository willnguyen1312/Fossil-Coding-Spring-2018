import { readData, writeData } from '../../utils/io'
import ultraNumberFunc from './3'

const pathIn = '/src/problem3/3.in'
const pathOut = '/src/problem3/3.out'

const inputTest = readData(`${pathIn}`).slice(1)
const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem3/3.out.nam'

describe('Problem 3', () => {
  it('should pass the sample tests', () => {
    const sample1 = '1'
    expect(ultraNumberFunc(sample1)).toBe('1')

    const sample2 = '501'
    expect(ultraNumberFunc(sample2)).toBe('105')

    const sample3 = '9901'
    expect(ultraNumberFunc(sample3)).toBe('1099')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      const result = ultraNumberFunc(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
