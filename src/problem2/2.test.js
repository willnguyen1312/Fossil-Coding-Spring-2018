import { readData, writeData } from '../../utils/io'
import ultraDecode from './2'

const pathIn = '/src/problem2/2.in'
const pathOut = '/src/problem2/2.out'

const inputTest = readData(`${pathIn}`)
const outputTest = readData(`${pathOut}`)

const writeOutPath = '/src/problem1/2.out.nam'

describe('Problem 2', () => {
  it('should pass the sample tests', () => {
    const sample1 = 'tiếng việt'
    expect(ultraDecode(sample1)).toBe('tiếq việt')

    const sample2 = 'rất nhạt nhẽo'
    expect(ultraDecode(sample2)).toBe("zất n'ạt n'ẽo")
  })

  it('should pass the real tests', () => {
    const output = []
    for (let i = 0; i < inputTest.length; i += 1) {
      const result = ultraDecode(inputTest[i])
      output.push(result)
      expect(result).toBe(outputTest[i])
    }

    writeData(writeOutPath, output.join('\n'))
  })
})
