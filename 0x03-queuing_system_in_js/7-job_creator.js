import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data array
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  // ... add the rest of the jobs here
];

jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code_2', jobData).save((err) => {
    if (err) {
      console.error('Notification job creation failed:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
