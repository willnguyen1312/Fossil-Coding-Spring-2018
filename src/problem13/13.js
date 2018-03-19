/**
 *
 *
 * @export
 * @param {Array<Array<String>>} input
 * @returns {String} result
 */
export default function ultraMatrix(input) {
  const max = Math.max(...input.map(x => x.length))

  let i = 0
  let result = ''

  while (i < max) {
    // eslint-disable-next-line
    input.forEach(value => {
      if (value[i]) {
        result += `${value[i]} `
      }
    })
    i += 1
  }
  return result.trim()
}
