build-grpc:
	python -m grpc_tools.protoc --proto_path=./myapp/protos/ --python_out=./myapp/gen_py --grpc_python_out=./myapp/gen_py ./myapp/protos/*.proto

run-client:
	


