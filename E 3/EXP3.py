import random
import hashlib
import time

shared_secret = "anshuman raj singh"
print("\nThe shared secret is :", shared_secret)

# Server side: generate nonce
nonce = random.randint(1541, 15165)
print("Nonce :", nonce)

# Add timestamp
initial_timestamp = str(time.time())   # convert to string
print("initial_timestamp :", initial_timestamp)

# Client side: generate hash (without timestamp, basic auth)
add = shared_secret + str(nonce)
client_hash = hashlib.sha256(add.encode()).hexdigest()
print("\nclient_hash :", client_hash)

# Add response timestamp
response_timestamp = str(time.time())
print("response_timestamp :", response_timestamp)

# Server side: generate hash (same as client)
server_hash = hashlib.sha256(add.encode()).hexdigest()
print("\nserver_hash :", server_hash)

# Compare
if client_hash == server_hash:
    print("\nAuthentication Successful , Hash is Matched")
else:
    print("\nAuthentication Failed , Hash Failed")

# Now: add timestamp for replay-attack protection
combine = shared_secret + str(nonce) + initial_timestamp
timestamped_client_hash = hashlib.sha256(combine.encode()).hexdigest()
print("\ntimestamped_client_hash :", timestamped_client_hash)
