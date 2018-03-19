import { readData, writeData } from '../../utils/io'
import ultraWake from './4'
import chunks from '../../utils/chunk'

const pathIn = '/src/problem4/4.in'
const pathOut = '/src/problem4/4.out'

let inputTest = readData(`${pathIn}`).slice(1)

inputTest.pop()
inputTest = chunks(inputTest, 2)
const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem4/4.out.nam'

describe('Problem 4', () => {
  it('should pass the sample tests', () => {
    const sample1 = ['1 10 4', '01:00 02:00 03:00 04:00']
    expect(ultraWake(sample1)).toBe('01:00')

    const sample2 = ['3 60 6', '01:00 01:30 02:00 03:00 03:30 03:40']
    expect(ultraWake(sample2)).toBe('03:40')

    const sample3 = ['2 10 1', '01:00']
    expect(ultraWake(sample3)).toBe('can not wake!')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      const result = ultraWake(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
