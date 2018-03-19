import { readData, writeData } from '../../utils/io'
import ultraDate from './10'

const pathIn = '/src/problem10/10.in'
const pathOut = '/src/problem10/10.out'

const inputTest = readData(`${pathIn}`).slice(1)

const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem10/10.out.nam'

describe('Problem 10', () => {
  it('should pass the sample tests', () => {
    const sample1 = '31/12/2017'
    expect(ultraDate(sample1)).toBe(365)

    const sample2 = '31/12/2016'
    expect(ultraDate(sample2)).toBe(366)

    const sample3 = '01/01/2020'
    expect(ultraDate(sample3)).toBe(1)
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraDate(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
