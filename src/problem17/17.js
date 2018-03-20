/**
 *
 *
 * @param {Number} num
 * @returns {Array<Number>} arrFibo
 */
function genFibo(num) {
  const result = []
  result[0] = 0
  result[1] = 1

  for (let i = 2; result[i - 1] < num; i += 1) {
    result[i] = result[i - 1] + result[i - 2]
  }

  return result
}

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraFibo(input) {
  const arrInput = input.split(' ').map(Number)
  const max = Math.max(...arrInput)

  const arrFibo = genFibo(max)

  let result = []

  for (let i = 0; i < arrInput.length - 1; i += 1) {
    const sub = arrFibo.filter((x) => {
      const check1 = x > arrInput[i] && x < arrInput[i + 1]
      const check2 = x < arrInput[i] && x > arrInput[i + 1]
      return check1 || check2
    })
    result.push(...sub)
  }

  result = result.filter(x => !arrInput.includes(x)).sort((a, b) => a - b)

  return Array.from(new Set(result)).join(' ')
}
