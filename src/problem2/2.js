const matchAll = require('string.prototype.matchall')

const map = {
  ch: 'c',
  tr: 'c',
  c: 'k',
  q: 'k',
  đ: 'd',
  gh: 'g',
  ph: 'f',
  ng: 'q',
  ngh: 'q',
  kh: 'x',
  th: 'w',
  d: 'z',
  r: 'z',
  nh: "n'",
}

export const reg = new RegExp(
  Object.keys(map)
    .sort()
    .reverse()
    .join('|'),
  'g',
)

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} output
 */
export default function ultraDecode(input) {
  let result = input
  const matches = [...matchAll(input, reg)].reverse()

  for (const match of matches) {
    const { index } = match
    result = result.slice(0, index) + map[match[0]] + result.slice(index + match[0].length)
  }
  return result
}
