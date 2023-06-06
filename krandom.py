"""
PSEVDO RANDOM MUDULE
"""
import secrets
from collections.abc import Generator
MODULE_IS_READ = 0
FAKE_IS_READ = 0
#print("KRANDOM")
MODULE_IS_READ = 1
def fake_print():
    """ FAKE PRINT TEST"""
    print("WELL TEST -----\n ;-------;\n")
    FAKE_IS_READ = 1
def fake_random(seed = 1682952000000,modulus = 50 ,increment= 3,multip= 777666777) -> Generator[int, None, None] :
    """ PSEVDORANDOM GENERATOR """
    while True:
        seed = (multip * seed + increment) % modulus
        print("FAKE_RANDOM SEED: ",seed)
def fake_fortuna():
    random_data =secrets.token_bytes(16)
    print("Random Data:",random_data.hex())
    random_number = secrets.randbelow(100) + 1
    print("Random number: ",random_number)
