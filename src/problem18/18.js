const numArr = Array.from({ length: 10 }, (v, i) => `${i}`)

const letterArr = Array.from({ length: 26 }, (v, i) => `${String.fromCharCode(i + 97)}`)

const finalArr = [...numArr, ...letterArr]

const { length } = finalArr

function rotate(char, turn) {
  const indexOfChar = finalArr.indexOf(char)

  const diff = turn % length

  const jumpTo = indexOfChar + diff

  const rot = jumpTo >= length ? jumpTo % length : jumpTo
  return finalArr[rot]
}

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {String} result
 */
export default function ultraRotate(input) {
  const [numTurns, str] = input.split(' ')

  return str
    .split('')
    .map(letter => rotate(letter, +numTurns))
    .join('')
}
