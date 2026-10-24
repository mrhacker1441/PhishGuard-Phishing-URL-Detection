from urllib.parse import urlparse
import ipaddress

def detect_phishing(url):
    score = 0
    reasons = []

    # Step 1: Check empty URL
    url = url.strip()

    if not url:
        return "Invalid URL", 0, ["Please enter a URL."]

    # Step 2: Add HTTPS if missing
    if "://" not in url:
        url = "https://" + url

    # Step 3: Extract URL information
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname

        if (
            parsed.scheme not in ("http", "https")
            or not hostname
            or any(char.isspace() for char in hostname)
        ):
            return "Invalid URL", 0, ["Please enter a valid URL."]

        # Step 4: Check HTTPS
        if parsed.scheme == "http":
            score += 20
            reasons.append("Website does not use HTTPS.")

        # Step 5: Check URL length
        if len(url) > 75:
            score += 15
            reasons.append("URL is unusually long.")

        # Step 6: Check IP address
        try:
            ipaddress.ip_address(hostname)
            score += 30
            reasons.append("URL uses an IP address instead of a domain.")
        except ValueError:
            pass

        # Step 7: Check @ symbol
        if "@" in parsed.netloc:
            score += 25
            reasons.append("URL contains an @ symbol.")

        # Step 8: Check suspicious keywords
        suspicious_words = [
            "verify", "update", "login",
            "password", "banking", "urgent"
        ]

        found_words = [
            word for word in suspicious_words
            if word in url.lower()
        ]

        if found_words:
            score += 10
            reasons.append(
                "Suspicious keywords found: " + ", ".join(found_words)
            )

                # Step 9: Check excessive subdomains
        try:
            ipaddress.ip_address(hostname)
            is_ip = True
        except ValueError:
            is_ip = False

        if not is_ip and hostname.count(".") >= 3:
            score += 15
            reasons.append("URL contains multiple subdomains.")
            
        # Step 10: Calculate final risk
        score = min(score, 100)

        if score >= 50:
            result = "High Risk"
        elif score >= 20:
            result = "Suspicious"
        else:
            result = "Low Risk"

        if not reasons:
            reasons.append("No suspicious indicators detected.")

        return result, score, reasons

    except ValueError:
        return "Invalid URL", 0, ["Unable to parse URL."]