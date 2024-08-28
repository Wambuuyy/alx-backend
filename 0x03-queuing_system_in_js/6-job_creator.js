import kue from 'kue';
import Redis from 'ioredis';

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (err) {
    console.error('Notification job creation failed:', err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Handle job events
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.log(`Notification job failed: ${err}`);
});
