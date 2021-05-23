// Return original array if min_size is less than array's size
// if min_size > original array's size, fill array with value until size is reached
// return the changed array
const pad = (array, minSize, value = null) => {
  if (minSize <= array.length) {
    return array;
  }

  while (array.length < minSize) {
    array.push(value);
  }

  return array;
}

module.exports = pad;