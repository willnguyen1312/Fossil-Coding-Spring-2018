// @ts-nocheck
const map = {
  0: 'khong',
  1: 'mot',
  2: 'hai',
  3: 'ba',
  4: 'bon',
  5: 'nam',
  6: 'sau',
  7: 'bay',
  8: 'tam',
  9: 'chin',
}

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraFormat(input) {
  let arrInput = input.split('')
  let result = ''
  if (arrInput[0] === '-') {
    result += 'am '
    arrInput.shift()
  }

  arrInput = arrInput.map(Number).reverse()

  if (arrInput.length === 1) {
    result += map[arrInput[0]]
    return result
  }

  //   while (arrInput.length !== 4) {
  //     arrInput.push(0)
  //   }

  arrInput.forEach((value, index) => {
    if (index === 0) {
      if (value === 5 && arrInput[1] !== 0) {
        result = 'lam'
      } else {
        result = `${map[value]}`
      }
    } else if (index === 1) {
      if (value === 1) {
        result = `muoi ${result}`
      } else if (value === 0) {
        result = `le ${result}`
      } else {
        result = `${map[value]} muoi ${result}`
      }
    } else if (index === 2) {
      result = `${map[value]} tram ${result}`
    } else {
      result = `${map[value]} nghin ${result}`
    }
  })
  result = result.split(' ')

  let last = result[result.length - 1]
  while (last === 'khong' || last === 'le') {
    result.pop()
    last = result[result.length - 1]
  }

  return result.join(' ')
}
