/**
 *
 *
 * @export
 * @param {Array<String>} input
 * @returns {Number} result
 */
export default function ultraMilk(input) {
  const [line, options] = input
  // eslint-disable-next-line
  const [student, budget, numOfChoices] = line.split(' ')

  const min = Math.min(...options
    .trim()
    .split(' ')
    .map(Number))
  const numMilkTea = Math.floor(+budget / min) ? Math.floor(+budget / min) - 1 : 0
  if (numMilkTea < +student) {
    return numMilkTea
  }
  return +student
}
