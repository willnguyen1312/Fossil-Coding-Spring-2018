import { readFileSync, writeFileSync } from 'fs-extra'

export const readData = (filepath) => {
  const data = readFileSync(`.${filepath}`, { encoding: 'utf-8' })
  return data.split('\n')
}

export const writeData = (filepath, data) => {
  writeFileSync(`.${filepath}`, data)
}
