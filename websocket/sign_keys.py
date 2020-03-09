import ed25519


class Security:

    @staticmethod
    def load_key_pairs():
        keys = dict()

        with open("signing_keys", "rb") as file:
            line = [line for line in file]

            keys['public'] = line[0][64:]
            keys['private'] = line[0][:64]

        return keys

    @staticmethod
    def generate():
        signing_key, verifying_key = ed25519.create_keypair()

        with open("signing_keys", "wb") as file:
            file.write(verifying_key.to_ascii(encoding='hex'))
            file.write(signing_key.to_ascii(encoding='hex'))

    @staticmethod
    def get_signature(msg):
        keys = Security.load_key_pairs()

        private = keys['private']
        signing_key = ed25519.SigningKey(private)

        return signing_key.sign(msg, encoding='base64')


    @staticmethod
    def validate(msg, sig):
        keys = Security.load_key_pairs()

        public = keys['private']
        verifying_key = ed25519.VerifyingKey(public, encoding="hex")
        try:
            verifying_key.verify(sig, msg, encoding="base64")
            print("GOOD")
        except ed25519.BadSignatureError:
            print("BAD")



if __name__ == "__main__":
    Security.generate()

    keys_ = Security.load_key_pairs()

    #msg_ = str(keys_['public']) + str(0)

    #sig_ = Security.get_signature(msg_.encode('utf-8'))
    #sig_ = Security.get_signature('hello')
    #Security.validate(msg_.encode('utf-8'), sig_)

