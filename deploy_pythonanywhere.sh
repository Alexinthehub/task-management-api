#!/bin/bash
echo "=== PythonAnywhere Deployment Script ==="

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

echo "=== Deployment preparation complete ==="
echo "Next steps:"
echo "1. Upload code to PythonAnywhere"
echo "2. Set environment variables in Web App configuration"
echo "3. Reload your web app"
EOL

# Make the script executable
chmod +x deploy_pythonanywhere.sh