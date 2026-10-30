import ipaddress
from urllib.parse import urlparse

def inspect_url(raw_url):
    warnings = []
    if "@" in raw_url:
        warnings.append("URL contains an @ symbol.")
    if len(raw_url) > 100:
        warnings.append("URL is longer than 100 characters.")

    parsed = urlparse(raw_url if "://" in raw_url else "http://" + raw_url)
    host = parsed.hostname or ""

    try:
        ipaddress.ip_address(host)
        warnings.append("Hostname is an IP address.")
    except ValueError:
        pass

    if len(host.split(".")) >= 5:
        warnings.append("Hostname has 5 or more labels.")
    if "xn--" in host.lower():
        warnings.append("Hostname contains a punycode marker (xn--).")
    if parsed.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS.")
    return warnings

def main():
    print("Phishing URL Awareness Checker")
    print("This tool checks URL text only. It does not open websites.")
    while True:
        url = input("\nEnter a URL (or q to quit): ").strip()
        if url.lower() in {"q", "quit", "exit"}:
            break
        if not url:
            print("Please enter a URL.")
            continue
        warnings = inspect_url(url)
        if warnings:
            print("\nREVIEW CAREFULLY")
            for item in warnings:
                print("- " + item)
        else:
            print("\nNo configured warning indicators found.")
        print("No warning does not prove that a URL is safe.")

if __name__ == "__main__":
    main()
