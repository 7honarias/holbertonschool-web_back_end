export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (var element of array) {
    newArray.push(appendString + element);
  }
  return newArray;
}
