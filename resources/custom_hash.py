import hashlib


def create_hash(time_stamp, passphrase):
    joined_string = time_stamp + passphrase
    h = hashlib.md5(joined_string.encode())
    return h.hexdigest()


def match_hash(time_stamp, passphrase, request_hash):
    created_hash = create_hash(time_stamp, passphrase)
    return created_hash == request_hash
