# required_package = ["python3", "pip", "requests", "boto3", "pip"]
# print(required_package)
# print("requests" in required_package)
# print("ansible" in required_package)
# is_request = "rexuests" in required_package

# is_ansible = "ansible" in required_package

# print(f"Is requests in the required_package list? {is_request}")
# print(f"Is ansible in the required_package list? {is_ansible}")

# required_package = set(required_package)
# required_package.add("paramiko")
# required_package.discard("pip")
# print(required_package)
# installed_packages = {"docker", "python3", "pip"}
# missing_packages = required_package - installed_packages
# print(missing_packages)
# extra_packages = installed_packages - required_package
# print(extra_packages)
# common_packages = required_package & installed_packages
# print(common_packages)

# 1. Required packages
required_packages = {"python3", "pip", "requests", "boto3"}

# 2. שינויים
required_packages.add("paramiko")
required_packages.discard("pip")

# 3. Installed packages
installed_packages = {"docker", "python3", "pip"}

# 4. חישובים
missing_packages = required_packages - installed_packages
extra_packages = installed_packages - required_packages
common_packages = required_packages & installed_packages

# 5. הדפסה
print(f"Missing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")