/**
 *
 *
 * @export
 * @param {Array<String>} input
 * @returns {String} result
 */
export default function ultraRank(input) {
  const [, grades] = input
  const arrGrades = grades.split(' ')

  const map = arrGrades.reduce((acc, cur) => {
    if (!acc[cur]) {
      acc[cur] = 1
    } else {
      acc[cur] += 1
    }
    return acc
  }, {})

  // @ts-ignore
  let entries = Object.entries(map).sort((a, b) => b[0] - a[0])
  let rank = 1

  for (const item of entries) {
    item.push(rank)
    rank += item[1]
  }

  entries = entries.reduce((acc, cur) => {
    const [key, , value] = cur
    acc[key] = value
    return acc
  }, {})

  return arrGrades.map(x => entries[x]).join(' ')
}
