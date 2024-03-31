rm -rf venv
python3 -m venv venv
if [[ "$OSTYPE" == "darwin"* ]]
then
    source ./venv/bin/activate

elif [[ "$OSTYPE" == "msys" ]]
then
    source ./venv/Scripts/activate


fi
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install --editable "."
pre-commit install
