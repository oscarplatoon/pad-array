const pad = require('./padArray');

test('test case 1', () => {
  expect(pad([1, 2, 3], 5)).toEqual([1, 2, 3, null, null]);
})

test('test case 2', () => {
  expect(pad([1, 2, 3], 5, 'apple')).toEqual([1, 2, 3, 'apple', 'apple']);
})

test('test case 3', () => {
  expect(pad([1, 2, 3], 3)).toEqual([1, 2, 3]);
})

test('test case 4', () => {
  expect(pad([1, 2, 3], 1)).toEqual([1, 2, 3]);
})