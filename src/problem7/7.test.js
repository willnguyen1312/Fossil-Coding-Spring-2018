import { readData, writeData } from '../../utils/io'
import ultraMilk from './7'
import chunks from '../../utils/chunk'

const pathIn = '/src/problem7/7.in'
const pathOut = '/src/problem7/7.out'

let inputTest = readData(`${pathIn}`).slice(1)

inputTest.pop()
inputTest = chunks(inputTest, 2)
const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem7/7.out.nam'

describe('Problem 7', () => {
  it('should pass the sample tests', () => {
    const sample1 = ['3 10 3', '1 2 3']
    expect(ultraMilk(sample1)).toBe(3)

    const sample2 = ['2 10 3', '5 5 5']
    expect(ultraMilk(sample2)).toBe(1)
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraMilk(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
