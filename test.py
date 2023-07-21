import raptoreum_hash
from binascii import unhexlify, hexlify

import unittest

# raptoreum block #1
# moo@b1:~/.raptoreum$ raptoreum-cli getblockhash 1
# 5c7aad59fd281029fba98b04a362d84843e579590e367f9cb0bbb3f9b6ee062b
# moo@b1:~/.raptoreum$ raptoreum-cli getblockheader 5c7aad59fd281029fba98b04a362d84843e579590e367f9cb0bbb3f9b6ee062b
#{
#  "hash": "5c7aad59fd281029fba98b04a362d84843e579590e367f9cb0bbb3f9b6ee062b",
#  "confirmations": 617540,
#  "height": 1,
#  "version": 536870912,
#  "versionHex": "20000000",
#  "merkleroot": "a9068d12f9c222ee11fb1a5d0ef8a98e9c4ccc88bf2dc5ddc2022b59e6104848",
#  "time": 1614374298,
#  "mediantime": 1614374298,
#  "nonce": 697,
#  "bits": "20001fff",
#  "difficulty": 4.768880961244323e-07,
#  "chainwork": "0000000000000000000000000000000000000000000000000000000000001000",
#  "nTx": 1,
#  "previousblockhash": "b79e5df07278b9567ada8fc655ffbfa9d3f586dc38da3dd93053686f41caeea0",
#  "nextblockhash": "f8907c309178109a4241133234ac4d5b1254e1839f1487a3b8155f0f79b75125",
#  "chainlock": true
#}
#moo@b1:~/.raptoreum$ raptoreum-cli getblockheader 5c7aad59fd281029fba98b04a362d84843e579590e367f9cb0bbb3f9b6ee062b false
#00000020a0eeca416f685330d93dda38dc86f5d3a9bfff55c68fda7a56b97872f05d9eb7484810e6592b02c2ddc52dbf88cc4c9c8ea9f80e5d1afb11ee22c2f9128d06a99a653960ff1f0020b9020000

header_hex = ("00000020a0eeca416f685330d93dda38dc86f5d3a9bfff55c68fda7a56b97872f05d9eb7484810e6592b02c2ddc52dbf88cc4c9c8ea9f80e5d1afb11ee22c2f9128d06a99a653960ff1f0020b9020000")

best_hash = '238408f6619db7d71175d359bd31d651fc02dcfdc84bc6d28da6436feda51f00'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_raptoreum_hash(self):
        self.pow_hash = hexlify(raptoreum_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

