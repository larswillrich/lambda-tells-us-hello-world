mkdir helloworld
pip3 install --target ./helloworld boto3
pip3 install --target ./helloworld json

cd helloworld
zip -r9 helloworld.zip .
zip -g helloworld.zip ../helloworld.py
cd ..

