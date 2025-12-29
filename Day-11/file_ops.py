## Update a server resources in the server.conf file up on external notification.

def update_server_config(file_path, key, new_value):
   with open(file_path, 'r') as file: 
      lines = file.readlines()
    #   print(lines)
   
   with open(file_path, 'w') as file:
      for line in lines: 
         if key in line:
            file.write(f"{key}={new_value}\n")   # Updating the line with new value
         else:
            file.write(line)

# Example usage:
update_server_config('C:/Python/Day01/server.config', "MAX_CONNECTIONS", "1000")
