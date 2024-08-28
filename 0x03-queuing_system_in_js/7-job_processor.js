import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define the blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Define the function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistedNumbers.includes(phoneNumber)) {
    job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

// Process the jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
