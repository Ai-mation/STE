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
pip install --editable ".[dev]"
pre-commit install
