# servers = ["web01", "web02", "web03" "db01", "db02"]
# print(servers)
# print(servers[0])
# print(servers[ : : 2])
deployment_targets = ["us-east-1", "eu-west-1", "ap-southeast-1"]
print(deployment_targets)
print(deployment_targets[0])
print(deployment_targets[1])
deployment_targets.append("us-west-2")
print(deployment_targets)
deployment_targets.append("extra-region")
deployment_targets[1] = "eu-central-1"
print(deployment_targets)
print(len(deployment_targets))