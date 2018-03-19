function delta(x1, y1, x2, y2) {
  return [x2 - x1, y2 - y1]
}

function parallel([dx1, dy1], [dx2, dy2]) {
  return dx1 * dy2 === dx2 * dy1
}

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraCoords(input) {
  const [x1, y1, x2, y2, x3, y3, x4, y4] = input.split(' ').map(Number)

  const d1 = delta(x1, y1, x2, y2)
  const d2 = delta(x3, y3, x4, y4)
  const d3 = delta(x1, y1, x3, y3)

  // @ts-ignore
  return parallel(d1, d2) && !parallel(d1, d3) ? 'YES' : 'NO'
}
