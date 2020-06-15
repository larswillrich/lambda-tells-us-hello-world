mkdir newEvent

pip3 install --target ./newEvent boto3
pip3 install --target ./newEvent json

cd newEvent
zip -r9 newEvent.zip .
zip -g newEvent.zip ../newEvent.py
cd ..

mkdir readEvent
pip3 install --target ./readEvent boto3
pip3 install --target ./readEvent json

cd readEvent
zip -r9 readEvent.zip .
zip -g readEvent.zip ../readEvent.py
cd ..

