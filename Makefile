OS := $(shell uname)
ifneq (,$(findstring MINGW64_NT,$(OS)))
	SHELL_TYPE := BASH
	DIR := env/Scripts/activate
else
	SHELL_TYPE := PWSH
	DIR := env\Scripts\activate
endif
ifeq ($(OS), Darwin)
	SHELL_TYPE := BASH
	DIR := env/bin/activate
endif
ifeq ($(SHELL_TYPE), PWSH)
	VENV := if not exist env
	SOURCE :=
	PASS := VER>NUL
	CLEAN := rmdir /s /Q
else
	VENV := test -d env/ ||
	SOURCE := source
	PASS := true
	CLEAN := rm -r
endif


all: setup

clean:
	$(CLEAN) env || $(PASS)

venv:
	$(VENV) python3 -m venv env

pip:
	$(SOURCE) $(DIR) && python -m pip install --upgrade pip

setup: clean venv pip
	$(SOURCE) $(DIR) && python -m pip install -Ur requirements.txt && python -m pip install -e .

lint: setup
	$(ACTIVATE); pre-commit install; pre-commit run --all-files --color always
