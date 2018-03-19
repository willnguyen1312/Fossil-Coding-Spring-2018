/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} output
 */
export default function ultraTrim(input) {
  let result = input.trim()
  result = result.replace(/([\s])+/g, '$1')
  return result
}
