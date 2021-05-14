check_virtualenv=$(which virtualenv)
if [ check_virtualenv == 1 ]; then
    echo "Installing virtual env"
    pip3 install virtualenv
fi
virtualenv -p python3 vaccine
source vaccine/bin/activate
pip install -r requirements.txt
python find_slot.py