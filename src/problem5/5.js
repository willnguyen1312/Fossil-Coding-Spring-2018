import { inRange } from 'lodash'

/**
 *
 *
 * @export
 * @param {String} input
 * @returns {Number} result
 */
export default function ultraLight(input) {
  const [numLights, position, left, right] = input.split(' ')

  if (+left === 1 && right === numLights) {
    return 0
  }

  if (+left === 1) {
    return Math.abs(+position - +right) + 1
  }

  if (right === numLights) {
    return Math.abs(+position - +left) + 1
  }

  if (inRange(+position, +left, +right + 1)) {
    const toLeft = +position - +left
    const toRight = +right - +position
    if (toLeft <= toRight) {
      return toLeft + (+right - +left) + 2
    }
    return toRight + (+right - +left) + 2
  }

  if (+position < +left) {
    // eslint-disable-next-line
    return +right - +position + 2
  }

  // eslint-disable-next-line
  return +position - +left + 2
}
