import sum from '../../utils/sum'

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {Number} result
 */
export default function ultraNum(input) {
  const arrInput = input.split('').map(Number)

  let result = arrInput.reduce(sum)

  while (`${result}`.length !== 1) {
    result = result
      .toString()
      .split('')
      .map(Number)
      .reduce(sum)
  }

  return result
}
