import sum from '../../utils/sum'

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {Number} result
 */
export default function ultraDate(input) {
  const [date, month, year] = input.split('/').map(Number)

  const uti = Array.from({ length: 12 }, (v, i) => i + 1).map(x => new Date(year, x, 0).getDate())

  return uti.slice(0, +month - 1).reduce(sum, 0) + date
}
