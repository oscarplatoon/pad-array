// Write unit tests!
const pad = require('./padArray')

test('properly pads arrays with given filler', () => {
  expect(pad([1,2,3], 'cat', 5)).toEqual([1,2,3,"cat","cat"])
})

test('refuse extra padding', () => {
  expect(pad([1,2,3], 'cat', 3)).toEqual([1,2,3])
})
