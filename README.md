# server_api

1. install packages from requirements.txt
2. from terminal execute 'python3 app.py'. The server should start running at port 8000
3. run the test file 'server_api_test.ipynb' from Jupyter notebook.

### Perrformance test

Performance test result for the /predict api.

```
tool used: JMeter
Java heap: HEAP="-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m"
no of threads used: 200 users
ramp-up period for sending requests: 1 sec
test perfomred in a MacBookPro with config:
processor: 2.6 GHz 6 core intel Core i7
memory: 16 GB 2400 MHz DDR4
```

After setting 200 requests/ sec in a thread group, the first 90 request was successful. Afterwards, on an average 3 out of 20 requests failed with Socket exception.

```
total request sent: 4000
test duration: 46 sec 188 milliseconds
server throughput: 85 per sec (approx.)
```

```Failure response sample result:
Thread Name:users 1-124
Sample Start:2023-05-29 19:42:26 CDT
Load time:101
Connect Time:100
Latency:0
Size in bytes:2455
Sent bytes:0
Headers size in bytes:0
Body size in bytes:2455
Sample Count:1
Error Count:1
Data type ("text"|"bin"|""):text
Response code:Non HTTP response code: java.net.SocketException
Response message:Non HTTP response message: Broken pipe

HTTPSampleResult fields:
ContentType:
DataEncoding: null
```

```Success response sample result:
Thread Name:users 1-127
Sample Start:2023-05-29 19:42:25 CDT
Load time:1580
Connect Time:299
Latency:1580
Size in bytes:188
Sent bytes:171
Headers size in bytes:166
Body size in bytes:22
Sample Count:1
Error Count:0
Data type ("text"|"bin"|""):text
Response code:200
Response message:OK

HTTPSampleResult fields:
ContentType: application/json
DataEncoding: null
```
