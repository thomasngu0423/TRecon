# TRecon - Tool for Reconnaissance and Google Dorking

TRecon is a versatile command-line tool that combines Google Dorking, Nmap scanning, reconnaissance techniques, and brute force directory enumeration. It is designed to assist in information gathering, vulnerability assessment, and penetration testing.

## Features

- **Google Dorking**: Perform targeted Google searches to discover sensitive information, exposed documents, configuration files, and more.
- **Nmap Scanning**: Scan target hosts or networks for open ports, running services, and potential vulnerabilities.
- **Reconnaissance**: Gather information about target domains, IP addresses, DNS records, WHOIS data, and SSL certificates.
- **Brute Force Directory Enumeration**: Enumerate directories and files on target web applications using wordlists or custom dictionaries.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/thomasngu0423/TRecon.git
   ```
   ```bash
   cd TRecon

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt

3. Run the script:

   ```bash
   python main.py

**Note:** 
1. Follow the prompts and select the desired option to perform reconnaissance or use Google Dorking.
2. For Nmap scanning, provide the target IP address or range and select the scan type.
3. For brute force directory enumeration, provide the target URL and select the wordlist or specify a custom dictionary.
4. Explore the results and analyze the gathered information.

## Dependencies

    Python 3.x
    requests module
    beautifulsoup4 module
    nmap module

## Supported Operating Systems
- Debian-based Linux distributions (e.g., Ubuntu)

## Contributions

Contributions to this project are welcome. Feel free to open issues and submit pull requests to contribute to the improvement of this tool.

## Disclaimer

TRecon is intended for educational and ethical purposes only. The developers are not responsible for any unauthorized use or misuse of this tool. Use it at your own risk.

