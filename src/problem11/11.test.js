import { readData, writeData } from '../../utils/io'
import ultraStreak from './11'
import chunks from '../../utils/chunk'

const pathIn = '/src/problem11/11.in'
const pathOut = '/src/problem11/11.out'

let inputTest = readData(`${pathIn}`)
  .slice(1)
  .map(x => x.trim())

inputTest = chunks(inputTest, 2)
const outputTest = readData(`${pathOut}`).map(x => x.trim())

const writeOutPath = '/src/problem11/11.out.nam'

describe('Problem 11', () => {
  it('should pass the sample tests', () => {
    const sample1 = ['10 20 15 17', '5 10 20 15']
    expect(ultraStreak(sample1)).toBe(2)

    const sample2 = ['5', '10']
    expect(ultraStreak(sample2)).toBe(0)

    const sample3 = [
      '968 1007 1257 1277 1185 1023 1180 942 1037 1027',
      '660 925 955 171 71 732 654 698 933 581',
    ]
    expect(ultraStreak(sample3)).toBe(10)
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      // @ts-ignore
      const result = ultraStreak(inputTest[i]).toString()
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
