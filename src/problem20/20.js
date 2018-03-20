/**
 *
 *
 * @export
 * @param {String} input
 * @returns {Number} result
 */
export default function ultraString(input) {
  const [sub, str] = input.split(' ')

  let index = 0
  let result = 0

  while (str.indexOf(sub, index) !== -1) {
    result += 1
    index = str.indexOf(sub, index) + 1
  }

  return result
}
