## Command Line Arguments & Environment Variables in Python

Python scripts are often executed from the command line, integrated into CI/CD pipelines, or run on servers. In such cases, passing inputs dynamically and handling sensitive information securely becomes very important.

This is where Command Line Arguments and Environment Variables are used.

### Command Line Arguments in Python

#### What are Command Line Arguments?

Command line arguments are inputs passed to a Python script at runtime from the terminal.

Example:

```python
python monitor.py server1 80
```

#### 📦 sys Module

The sys module is used to read command line arguments in Python.

```python
import sys
print(sys.argv)
```

sys.argv is a list
* sys.argv[0] → script name
* sys.argv[1] → first argument
* sys.argv[2] → second argument

###### DevOps Use Cases

* Passing environment name (dev, prod)
* Passing server IP or hostname
* Running scripts in CI/CD pipelines with different parameters

#### socket Module – Reading Server Name

The socket module is used to interact with network-related information.

```python
import socket

hostname = socket.gethostname()
print(hostname)
```
Use Case:

* Identify which server the script is running on
* Useful in monitoring, logging, and debugging

#### psutil Module – System Monitoring

The psutil module is widely used in DevOps for system-level monitoring.

What can it do?

* CPU usage
* Memory usage
* Disk usage
* Running processes

```python
import psutil

print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)
```

#### Installing & Checking psutil

```python
pip install psutil
pip show psutil
```

#### Environment Variables in Python

Environment variables store key–value pairs at the OS level and are commonly used to store sensitive information.

Examples of Sensitive Data:

* API keys
* Passwords
* Tokens
* Certificates
* Private keys

#### Why DevOps Engineers Use Environment Variables?

* Avoid hardcoding secrets in code
* Secure configuration management
* Easy integration with CI/CD tools (Jenkins, GitHub Actions, GitLab)

#### Setting Environment Variables Manually (Linux)

```python
export password="Vibhuti"
export apitoken="sssdddffffwww"
```

##### Reading Environment Variables in Python

```python
import os

print(os.getenv("password"))
print(os.getenv("apitoken"))
```

#### Difference: Command Line Arguments vs Environment Variables

| Feature    | Command Line Argument | Environment Variable  |
| ---------- | --------------------- | --------------------- |
| Visibility | Visible in terminal   | Hidden from command   |
| Security   | ❌ Not secure          | ✅ Secure              |
| Usage      | Runtime parameters    | Sensitive information |
| Scope      | Script-specific       | OS / session-wide     |
| DevOps Use | Script configuration  | Secrets & credentials |
