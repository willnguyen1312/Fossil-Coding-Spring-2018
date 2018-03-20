/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraShorten(input) {
  let str = input
  let index = 0
  while (index < str.length) {
    for (let i = 0; i < str.length; i += 1) {
      if (str[i] === str[i + 1]) {
        str = str.substring(0, i) + str.substring(i + 2)
        index = 0
        break
      }
      index += 1
    }
  }
  return str || 'Empty String'
}
