import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('ready', () => console.log('Redis client connected to the server'));
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
  return (schoolName, value);
}
const promise = promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
  const response = await promise(schoolName);
  console.log(response);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
