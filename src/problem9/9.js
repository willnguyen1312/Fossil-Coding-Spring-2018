/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraRemove(input) {
  return Array.from(new Set(input.split(' '))).join(' ')
}
