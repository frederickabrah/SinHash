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
