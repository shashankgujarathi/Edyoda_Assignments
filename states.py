import json

indian_states = {
    "Andhra Pradesh": "Amaravati",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Maharashtra": "Mumbai",
    "Gujarat": "Gandhinagar",
    "Kerala": "Thiruvananthapuram"
}
file = open("indian_states.json", "w")
json.dump(indian_states,file)

print("Data has been written to 'indian_states.json'")
