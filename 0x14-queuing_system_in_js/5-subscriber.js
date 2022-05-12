import { createClient } from 'redis';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('ready', () => console.log('Redis client connected to the server'));

const hsChannel = 'holberton school channel';
client.subscribe(hsChannel);
client.on('message', (channel, message) => {
  if (channel === hsChannel) console.log(message);

  if (message === 'KILL_SERVER') {
    client.unsubscribe(hsChannel);
    client.quit();
  }
});
