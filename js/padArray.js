// REMEMBER TO PSEUDOCODE
function pad(array, minSize, value) {
  var returnArray = array
  while (array.length < minSize) {
    returnArray.push(value)
  }
return returnArray
}

module.exports = pad