check_virtualenv=$(which virtualenv)
if [ check_virtualenv == 1 ]; then
    echo "Installing virtual env"
    pip3 install virtualenv
fi
echo;echo
echo "______________________Creating VirtualEnv called vaccine____________________";echo;echo

virtualenv -p python3 vaccine;echo;echo
echo "______________________VirtualEnv CREATED____________________";echo;echo
source vaccine/bin/activate
echo;echo
echo "______________________Installing Requirements____________________";echo;echo
pip install -r requirements.txt
echo;echo
echo "______________________Executing Vaccine Slot Notifier____________________";echo;echo
nohup python find_slot.py &