## Example: Automating a log file analysis with a loop to find errors.

log = ["2025-03-01 10:00:12 INFO  Application started" ,
       "2025-03-01 10:00:13 INFO  Loading configuration file", 
       "2025-03-01 10:00:14 INFO  Database connection established",
       "2025-03-01 10:01:02 ERROR Failed to fetch user data: timeout occurred",
       "2025-03-01 10:01:05 INFO  Retrying database request",
       "INFO: Operation successful",
       "ERROR: File not found",
       "DEBUG: Connection established",
       "ERROR: Database connection failed",]

for entry in log: 
    if "INFO" in entry:
        print(entry)
