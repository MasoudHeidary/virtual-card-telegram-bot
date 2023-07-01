from flutterwave_python.rave import Rave
import os

os.environ['RAVE_PUBLIC_KEY'] = 'FLWPUBK-851f22eddbb76aa7c96af35ffc176c7f-X'
os.environ['RAVE_SECRET_KEY'] = 'FLWSECK-bfb04d81ae12273a23c732c699008017-X'
os.environ['RAVE_ENCRYPTION_KEY'] = 'bfb04d81ae12bd949dba20ed'

rave = Rave(
    secretKey=os.getenv('RAVE_SECRET_KEY'),
    encryptionKey=os.getenv('RAVE_ENCRYPTION_KEY'),
    publicKey=os.getenv('RAVE_PUBLIC_KEY'),
)
