#!/bin/bash

# 📁 Path where Jenkins keeps job logs
JENKINS_LOG_DIR="/var/jenkins_home/jobs"

# ☁️ Your S3 bucket name
S3_BUCKET="your-s3-bucket-name"

# 📅 How many days old logs to archive
DAYS_OLD=7

# 📝 Log file
LOG_FILE="/var/log/jenkins_log_archive.log"

# 🔁 Find and process old log files
find "$JENKINS_LOG_DIR" -name "log" -type f -mtime +$DAYS_OLD | while read -r logfile; do
    echo "Processing: $logfile"

    # 📦 Compress the log
    gzip -f "$logfile"
    COMPRESSED_FILE="${logfile}.gz"

    # 🗂 Create relative path for S3 (remove base path)
    RELATIVE_PATH="${COMPRESSED_FILE#$JENKINS_LOG_DIR/}"

    # ☁️ Upload to S3
    aws s3 cp "$COMPRESSED_FILE" "s3://$S3_BUCKET/jenkins-logs/$RELATIVE_PATH"

    if [ $? -eq 0 ]; then
        echo "$(date): Uploaded and removing $COMPRESSED_FILE" >> "$LOG_FILE"
        rm -f "$COMPRESSED_FILE"
    else
        echo "$(date): Failed to upload $COMPRESSED_FILE" >> "$LOG_FILE"
    fi
done
