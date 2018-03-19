const reg = /^0+(\d+)/

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraDict(input) {
  const arrInput = input.split(' ').map(x => x.replace(reg, '$1'))

  // @ts-ignore
  return arrInput.sort((a, b) => a.localeCompare(b)).join(' ')
}
