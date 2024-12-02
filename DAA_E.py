'''We are given a sequence of N goods of production numbered from 1 to N. Each good has a
 volume denoted by (Vi). The constraint is that once a good has been completed its volume
 starts decaying at a fixed percentage (P) per day. All goods decay at the same rate and further
 each good takes one day to complete. 
We are required to find the order in which the goods should be produced so that the overall
 volume of goods is maximized'''


def maximize_volume(volumes, decay_rate):
    volumes.sort(reverse=True)  # Sort in descending order
    total_volume = 0
    t = 0
    for v in volumes:
        total_volume += v * ((1 - decay_rate) ** t)
        t += 1
    return total_volume

# Inputs
volumes = [151, 15, 1, 52]
decay_rate = 0.1
result = maximize_volume(volumes, decay_rate)
print(f"Maximum Volume: {result:.2f}")
