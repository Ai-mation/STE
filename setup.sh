rm -rf venv
python3 -m venv env
if [[ "$OSTYPE" == "darwin"* ]]
then
    source ./env/bin/activate

elif [[ "$OSTYPE" == "msys" ]]
then
    source ./env/Scripts/activate


fi
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install --editable "."
pre-commit install
