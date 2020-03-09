import ed25519


class Security:

    @staticmethod
    def generate():
        privKey, pubKey = ed25519.create_keypair()

        keys = dict()
        keys['public'] = pubKey
        keys['private'] = privKey

        return(keys)


    @staticmethod
    def get_signature(msg):
        keys = Security.generate()

        privKey = keys['private']
        signature = privKey.sign(msg, encoding='hex')
        return(signature)

    @staticmethod
    def validate(msg):
        keys = Security.generate()

        privKey = keys['private']
        pubKey = keys['public']
        signature = privKey.sign(msg, encoding='hex')
        try:
            pubKey.verify(signature, msg, encoding='hex')
            print("The signature is valid.")
        except:
            print("Invalid signature!")


if __name__ == "__main__":
    keys_ = Security.generate()
    print(keys_)

    msg = b'Mensaje de prueba'

    s = Security.get_signature(msg)
    print(s)

    Security.validate(msg)