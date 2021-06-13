# Network Latencies!

To help debug issues, Redia has a special mode for monitoring command latency. The redis latency-monitor-threshold directive sets a limit in  milliseconds that will log all or some of the commands and activity of Redis instance that exceed that limit with a defualt 0.

```bash
127.0.0.1:6379> CONFIG SET latency-monitor-threshold 100
OK
127.0.0.1:6379> DEBUG SLEEP 1
OK
(1.00s)
127.0.0.1:6379> DEBUG SLEEP .25
OK
127.0.0.1:6379> LATENCY LATEST
1) 1) "command"
   2) (integer) 1623580902 # timestamp of latest latency
   3) (integer) 250 # Latest latency occured for time, DEBUG SLEEP 0.25
   4) (integer) 1000  # DEBUG SLEEP 1
127.0.0.1:6379> LATENCY HISTORY command # Latest 160 latencies.
1) 1) (integer) 1623580898
   2) (integer) 1000
2) 1) (integer) 1623580902
   2) (integer) 250
127.0.0.1:6379> DEBUG SLEEP .5
OK
(0.50s)
127.0.0.1:6379> DEBUG SLEEP .3
OK
127.0.0.1:6379> DEBUG SLEEP .8
OK
(0.80s)
127.0.0.1:6379> DEBUG SLEEP .2
OK
127.0.0.1:6379> DEBUG SLEEP .6
OK
(0.60s)
127.0.0.1:6379> LATENCY GRAPH command
command - high 1000 ms, low 200 ms (all time high 1000 ms)
#  _
|   | _
| o | |
|_|o|_|
       
7711119
mm9531s
  ssss 
```