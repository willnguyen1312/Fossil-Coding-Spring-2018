/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraLocal(input) {
  const arrInput = input.split(' ').map(Number)
  let isLocal = true
  const result = []
  const { length } = arrInput

  for (let i = 0; i < length; i += 1) {
    isLocal = false

    if (i - 1 < 0) {
      isLocal = false
    } else if (i + 1 >= length) {
      isLocal = false
    } else if (arrInput[i] < arrInput[i - 1] && arrInput[i] < arrInput[i + 1]) {
      isLocal = true
    } else if (arrInput[i] > arrInput[i - 1] && arrInput[i] > arrInput[i + 1]) {
      isLocal = true
    }

    if (isLocal) {
      result.push(i)
    }
  }

  return result.join(' ')
}
