Rem This program is used to create and setup the bot and it's virtual environment
Rem Only run this program if you have python 3.10 on PATH

Rem go to correct folder
cd ..

Rem create virtual environment
python -m venv venv

Rem go to src folder
cd src

Rem activate virtual environment
call ../venv/Scripts/activate

Rem install requirements
pip install -r ../util/requirements.txt

Rem deactivate virtual environment
deactivate
