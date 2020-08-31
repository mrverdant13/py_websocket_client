clear
echo "Setting up..."

if [ ! -d ./venv ]
then
    clear
    echo "Creating virtual env..."
    virtualenv venv
fi

clear
echo "Installing packages (venv scope)..."
source venv/bin/activate
pip3 install -r linux-requirements.txt

# if [ ! -f ./app/secrets.py ]
# then
#     clear
#     echo "Generating 'secrets.py' file..."
#     cp ./app/secrets_schema.py ./app/secrets.py
# fi

# sudo nano app/secrets.py

# clear
# # echo "All done!"
# python3 ./app/app.py