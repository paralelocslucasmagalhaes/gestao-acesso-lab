run:
	export GOOGLE_APPLICATION_CREDENTIALS=${PWD}/creds/key.json && \
	export FIRESTORE_EMULATOR_HOST="[::1]:8567" && \
	uvicorn main:app --host 0.0.0.0 --reload