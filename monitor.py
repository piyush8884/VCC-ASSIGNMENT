import psutil
import time
import subprocess

CPU_THRESHOLD = 75

AMI = "ami-xxxxxxxx"
SG = "sg-xxxxxxxx"
KEY_NAME = "autoscale-demo-key"

while True:
   cpu = psutil.cpu_percent(interval=1)
   print(f"CPU Usage: {cpu}%")

   if cpu > CPU_THRESHOLD:
       print("Threshold exceeded → launching AWS instance")

       subprocess.run([
           "aws", "ec2", "run-instances",
           "--image-id", AMI,
           "--count", "1",
           "--instance-type", "t2.micro",
           "--key-name", KEY_NAME,
           "--security-group-ids", SG,
           "--user-data", "file:///home/lenovo/autoscale_demo/aws/user-data.sh"
       ])
       break

   time.sleep(5)
