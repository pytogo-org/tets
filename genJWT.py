import jwt
import datetime
import time

# PASTE YOUR EXACT JWT_SECRET FROM THE VM'S .env HERE
YOUR_JWT_SECRET = "f5ca66e4c2eb271f17ac3a78c9d865f01a50a7cf3082c306dc6ebda43be5e9ea195bc7a79bd8792a"

# Define common claims for Supabase keys
current_time_unix = int(time.time())
# Expiry 10 years from now
expiry_time_unix = int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365 * 10)).timestamp())

# Payload for ANON_KEY
anon_payload = {
    "role": "anon",
    "iss": "supabase",
    "iat": current_time_unix,
    "exp": expiry_time_unix,
    "aud": "authenticated" # Supabase often uses 'authenticated' for both, or 'anon' for anon key
}

# Payload for SERVICE_ROLE_KEY
service_role_payload = {
    "role": "service_role",
    "iss": "supabase",
    "iat": current_time_unix,
    "exp": expiry_time_unix,
    "aud": "authenticated"
}

# Encode the tokens
anon_key = jwt.encode(anon_payload, YOUR_JWT_SECRET, algorithm="HS256")
service_role_key = jwt.encode(service_role_payload, YOUR_JWT_SECRET, algorithm="HS256")

print(f"--- New Supabase Keys (Generated with JWT_SECRET from VM) ---")
print(f"ANON_KEY={anon_key}")
print(f"SERVICE_ROLE_KEY={service_role_key}")
print(f"----------------------------------------------------------")
print(f"Remember to replace the values in your VM's .env and restart docker-compose.")
print(f"Then replace SUPABASE_KEY in your Python project with the new SERVICE_ROLE_KEY.")
