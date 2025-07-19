#!/bin/bash

echo "$(date): Running file move..." >> /tmp/cron_debug.log
mv /workspaces/AWS-Boto3-Python/source/* /workspaces/AWS-Boto3-Python/destination/ >> /tmp/cron_debug.log 2>&1



# ✅ Step 1: Make the script executable
# Type: chmod +x /workspaces/AWS-Boto3-Python/ShellScripts/every5min_move_files.sh

# ✅ Step 2: Test the script manually
# Type: /workspaces/AWS-Boto3-Python/ShellScripts/every5min_move_files.sh

# ✅ Step 3: Update crontab for testing (run every 1 min)
# Type: crontab -e
# Add the following line to run the script every 5 minutes
# Add this line:
# Type in editor: * * * * * /bin/bash /workspaces/AWS-Boto3-Python/ShellScripts/every5min_move_files.sh
# *******We can add multiple lines for different scripts if needed.*******

# ✅ Step 4: Save and exit the editor
# For nano, press Ctrl+X, then Y, then Enter.

# ✅ Step 5: Verify the crontab entry
# Type: crontab -l
# You should see the entry you just added.

# ✅ Step 6: Check the log file for output
# Type: tail -f /tmp/cron_debug.log