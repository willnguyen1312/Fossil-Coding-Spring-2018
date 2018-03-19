/**
 *
 *
 * @param {String} hourTime
 * @returns {Number} minute(s)
 */
function hourToMinute(hourTime) {
  const [hour, minute] = hourTime.split(':')
  // eslint-disable-next-line
  return +hour * 60 + +minute
}

/**
 *
 *
 * @export
 * @param {Array<String> | String } input
 * @returns {String} result
 */
export default function ultraWake(input) {
  const [line, wakeupTimes] = input

  const arrLine = line.split(' ')
  const arrTime = wakeupTimes.split(' ')

  if (arrLine[2] === '0' || +arrLine[0] > +arrLine[2]) {
    return 'can not wake!'
  } else if (arrLine[0] === '1') {
    return arrTime[0]
  }
  const arrTimeInMinutes = arrTime.map(hourToMinute)
  const { length } = arrTimeInMinutes

  // eslint-disable-next-line
  for (let i = 0; i < length - +arrLine[0] + 1; i += 1) {
    for (let j = i; j < length; j += 1) {
      // eslint-disable-next-line
      const diff = arrTimeInMinutes[j] - arrTimeInMinutes[i] + 1

      if (diff > +arrLine[1]) {
        break
      }
      // eslint-disable-next-line
      const times = j - i + 1
      if (diff <= +arrLine[1] && times === +arrLine[0]) {
        return arrTime[j]
      }
    }
  }

  return 'can not wake!'
}
