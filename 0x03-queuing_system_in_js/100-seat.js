const express = require('express');
const { getAsync, setAsync } = require('./redisClient');
const queue = require('./queue');
const app = express();
const PORT = 1245;

let reservationEnabled = true;

// Set initial available seats
(async () => {
  await setAsync('available_seats', 50);
})();

// Function to reserve seats
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Function to get current available seats
const getCurrentAvailableSeats = async () => {
  return await getAsync('available_seats');
};

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const availableSeats = await getCurrentAvailableSeats();
      const newAvailableSeats = parseInt(availableSeats, 10) - 1;

      if (newAvailableSeats < 0) {
        done(new Error('Not enough seats available'));
      } else {
        await reserveSeat(newAvailableSeats);

        if (newAvailableSeats === 0) {
          reservationEnabled = false;
        }
        done();
      }
    } catch (error) {
      done(error);
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
