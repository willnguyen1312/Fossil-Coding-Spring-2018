import { readData, writeData } from '../../utils/io'
import ultraFormat from './6'

const pathIn = '/src/problem6/6.in'
const pathOut = '/src/problem6/6.out'

const inputTest = readData(`${pathIn}`).slice(1)
inputTest.pop()
const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem6/6.out.nam'

describe('Problem 6', () => {
  it('should pass the sample tests', () => {
    const sample1 = '15'
    expect(ultraFormat(sample1)).toBe('muoi lam')

    const sample2 = '101'
    expect(ultraFormat(sample2)).toBe('mot tram le mot')

    const sample3 = '2002'
    expect(ultraFormat(sample3)).toBe('hai nghin khong tram le hai')

    const sample4 = '-1'

    expect(ultraFormat(sample4)).toBe('am mot')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      const result = ultraFormat(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
