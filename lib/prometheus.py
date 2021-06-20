import prometheus_client as prom

algoHashrates = prom.Gauge('algo_hashrate', "The hashrate of a algorithm", ["algo"], 'hiveos')
invalidShares = prom.Gauge('invalid_shares', "The ratio of invalid shares of a algorithm", ["algo"], 'hiveos')

hashrates = prom.Gauge('hashrate', "The hashrate of a gpu or asic", ["device"], 'hiveos')
temperature = prom.Gauge('temperature', "The temperature of a gpu or asic", ["device"], 'hiveos')
