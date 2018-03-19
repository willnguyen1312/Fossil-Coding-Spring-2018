/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} output
 */
export default function ultraNumberFunc(input) {
  if (input.length === 1) {
    return input
  }

  const arrNum = input.split('').sort((a, b) => +a - +b)

  let index = 0

  while (+arrNum[index] === 0) {
    index += 1
  }

  [arrNum[0], arrNum[index]] = [arrNum[index], arrNum[0]]

  return arrNum.join('')
}
