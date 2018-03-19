/**
 *
 *
 * @export
 * @param {Array<String>} input
 * @returns {Number} result
 */
export default function ultraStreak(input) {
  let result = 0
  let current = 0
  const [step, goal] = input
  const arrStep = step.split(' ').map(Number)
  //   if (!goal) {
  //     console.log(input)
  //   }
  const arrGoal = goal.split(' ').map(Number)

  const { length } = arrGoal

  for (let i = 0; i < length; i += 1) {
    if (arrStep[i] >= arrGoal[i]) {
      current += 1
    } else {
      current = 0
    }
    result = result >= current ? result : current
  }

  return result
}
