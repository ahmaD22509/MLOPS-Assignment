PYTHON=python3

setup:
	pip install -r requirements.txt

download-data:
	cd src && $(PYTHON) load_data.py

preprocess: download-data
	cd src && $(PYTHON) preprocess.py

features: preprocess
	cd src && $(PYTHON) features.py

train: features
	cd src && $(PYTHON) train.py

predict: train
	cd src && $(PYTHON) predict.py

evaluate: predict
	cd src && $(PYTHON) evaluate.py

all: setup download-data preprocess features train predict evaluate

clean:
	rm -rf data/raw/*
	rm -rf data/processed/*
	rm -rf features/*
	rm -rf models/*
	rm -rf results/*
	find . -type d -empty -delete

.PHONY: setup download-data preprocess features train predict evaluate all clean
