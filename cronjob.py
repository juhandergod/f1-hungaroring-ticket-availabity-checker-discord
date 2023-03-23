from cron import CronTab

# Create a new cron job
my_cron = CronTab(user='myusername')

# Add a new job to the cron tab
job = my_cron.new(command='python3 main.py')
job.setall('*/5 * * * *') # run the job every 5 minutes

# Save the cron tab
my_cron.write()