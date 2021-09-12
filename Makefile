PYTHON=poetry
CHECK_SYNTAX=black
DEVELOPER=0
ARGS="-o codegen/tmp.py"

default: fmt
	DEVELOPER=$(DEVELOPER) $(PYTHON) run python codegen.py $(ARGS)

dep:
	$(PYTHON) install

fmt:
	$(PYTHON) run $(CHECK_SYNTAX) .

check:
	$(PYTHON) run pytest tests

env:
	$(PYTHON) shell

clean:
	rm -rf .venv **/__p* codegen/*