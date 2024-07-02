# Hash Cracking Tool - SINISTER X

This project is an advanced hash cracking tool designed to crack hashed passwords using various techniques. It supports multiple hash algorithms, wordlist-based attacks, and the use of precomputed rainbow tables. The tool also includes enhancements such as progress indication, logging, and error handling.

## Features

- Supports multiple hash algorithms (default: SHA-256)
- Wordlist-based attacks
- Rainbow table support
- Progress bar
- Logging of important events and results
- Graceful error handling

## Requirements

- Python 3
- `pyfiglet` for creating the 3D banner
- `termcolor` for colored text output
- `colorama` for colored console output
- `tqdm` for the progress bar

## Setup

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/frederickabrah/SinHash 
    ```

2. **Run the setup script**:
    ```sh
    chmod +x setup.sh
    ./setup.sh
    ```

## Usage

Run the hash cracking tool with the following command:

```sh
python3 hashcrack.py <target_hash> <wordlist> [options]
```

### Options

- `-t`, `--hash-type`: Specify the hash algorithm (default: sha256)
- `-s`, `--salt`: Specify an optional salt value
- `-r`, `--rainbow-table`: Specify the path to a precomputed rainbow table
- `-b`, `--benchmark`: Display benchmarking information

### Example

```sh
python3 hashcrack.py d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2 wordlist.txt -t sha256
```

## Error Handling

The tool includes robust error handling. If you interrupt the process with `Ctrl+C`, it will exit gracefully without displaying a traceback.

## Logging

All important events and results are logged in `hashcrack.log`.

## Banner

The tool displays a colorful 3D banner "SINISTER X" in red with a green shadow at the start of execution.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This tool was developed to assist with ethical hacking and penetration testing. Use responsibly and with permission.

```

### Explanation:
- **Introduction**: Brief description of the project.
- **Features**: Highlight key features of the tool.
- **Requirements**: List of required dependencies.
- **Setup**: Instructions for setting up the environment and installing dependencies.
- **Usage**: How to run the tool, including options and examples.
- **Error Handling**: Information about how errors are handled.
- **Logging**: Details about logging.
- **Banner**: Description of the banner displayed by the tool.
- **License**: Licensing information.
- **Acknowledgments**: Note about ethical use.

This `README.md` provides a comprehensive overview of the project, guiding users through setup, usage, and additional details.

## Dependencies

To ensure the script runs correctly, the following Python libraries are required:

- `pyfiglet`
- `termcolor`
- `colorama`
- `tqdm`

These libraries are automatically installed when you run the `setup.sh` script.

## Setup Script

The `setup.sh` script will handle the installation of all necessary dependencies. Here's the content of the `setup.sh` script for reference:

```sh
#!/bin/bash

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

# Install Python and pip
echo "Installing Python and pip..."
sudo apt install -y python3 python3-pip

# Install required libraries
echo "Installing required Python libraries..."
pip3 install pyfiglet termcolor colorama tqdm

# Optional: Install other tools that might be useful (e.g., git, build-essential)
echo "Installing additional tools..."
sudo apt install -y git build-essential

echo "Setup complete. You can now run the hash cracking script."
```

## Wordlist

The wordlist is a text file containing potential passwords. Each line in the wordlist should contain a single password. You can find various wordlists online or create your own.

## Rainbow Table

A rainbow table is a precomputed table for reversing cryptographic hash functions, primarily for cracking password hashes. If you have a rainbow table, you can specify its path using the `--rainbow-table` option. The file should be formatted with each line containing a word and its corresponding hash, separated by a colon.

### Example Format:

```
password1:5baa61e4c9b93f3f0682250b6cf8331b
password2:6cb75f652a9b52798eb6cf2201057c73
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Support

If you encounter any issues or have any questions, feel free to open an issue on the repository or contact the maintainer.

## Disclaimer

This tool is intended for educational purposes and ethical hacking only. Use it responsibly and ensure you have permission to test the security of the system you are working on. The author is not responsible for any misuse or damage caused by this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Additional Sections:
- **Dependencies**: Lists the Python libraries required for the script.
- **Setup Script**: Provides the content of the setup script for reference.
- **Wordlist**: Explains the format and use of wordlists.
- **Rainbow Table**: Details the format and use of rainbow tables.
- **Contributing**: Guidelines for contributing to the project.
- **Support**: Instructions on how to get help.
- **Disclaimer**: A note on ethical use and responsibility.
- **License**: Licensing information.

This `README.md` now covers all essential aspects of the project, providing clear instructions and useful information for users and contributors.
