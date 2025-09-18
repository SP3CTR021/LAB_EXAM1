def get_network(mobile_number):
    # Dictionary of networks with their key digits
    networks = {
        "Smart": ["13", "14", "20", "21", "28", "29", "30"],
        "TNT": ["09", "10", "11", "12", "18", "19"],
        "Sun": ["22", "23", "32", "33"],
        "Globe": ["15", "16", "17", "25", "26", "27"],
        "TM": ["03", "04", "05", "06", "07"],
        "Red": ["01", "02", "24"],
        "Dito": ["91", "92", "93", "94", "95", "96", "97", "98"]
    }

    # Check if input is valid
    if len(mobile_number) != 11 or not mobile_number.isdigit():
        return "Invalid number! Must be 11 digits."

    if not mobile_number.startswith("09"):
        return "Invalid number! Must start with 09."

    # Extract key digits (3rd and 4th digit)
    key = mobile_number[2:4]

    # Find matching network
    for network, keys in networks.items():
        if key in keys:
            return f"The network of the mobile number is {network}"

    return "Unknown network!"


# Main program
mobile_number = input("Enter a mobile number: ")
print(get_network(mobile_number))
