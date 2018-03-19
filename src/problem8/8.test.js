import { readData, writeData } from '../../utils/io'
import ultraRank from './8'
import chunks from '../../utils/chunk'

const pathIn = '/src/problem8/8.in'
const pathOut = '/src/problem8/8.out'

let inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

inputTest.pop()
inputTest = chunks(inputTest, 2)
const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem8/8.out.nam'

describe('Problem 8', () => {
  it('should pass the sample tests', () => {
    const sample1 = ['5', '10 10 10 9 9']
    expect(ultraRank(sample1)).toBe('1 1 1 4 4')

    const sample2 = ['3', '9 10 9']
    expect(ultraRank(sample2)).toBe('2 1 2')

    const sample3 = ['8', '1 0 6 8 3 2 0 9']
    expect(ultraRank(sample3)).toBe('6 7 3 2 4 5 7 1')
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraRank(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
