from hashlib import sha256
from tqdm import tqdm
MAX_INT_32 = 2**32
MAX_INT_64 = 2**64

def get_init_val(kerberos):
	#
	# kerberos: List<String> list of team member's kerberos
	# Returns: 64-int hash for m_0
	#
	# DO NOT CHANGE THIS FUNCTION
	#
	val = '||'.join(sorted(kerberos))
	return int(sha256(val.encode('utf-8')).hexdigest()[:16], 16)


def key_gen(msg):
    #
	# msg: 64-bit integer
	# Returns: random 64-bit key
	#
	# DO NOT CHANGE THIS FUNCTION
	#
	t = 20
	hex_size = 16
	mask = 2 ** t - 1

	msg_bytes = msg.to_bytes(8, 'big')
	hash_val = sha256(msg_bytes).hexdigest()[-hex_size:]
	full_key = int(hash_val.encode('utf-8'), hex_size)
	b = full_key & mask
	a = ((full_key >> t) & mask) | 1
	return a, b


def swap(m):
    most_sig = (m << 32) % MAX_INT_64
    least_sig = m >> 32
    return most_sig + least_sig


def linear(m, a, b):
	# YOUR WORK GOES HERE
	return (a*m + b) % MAX_INT_64


def encrypt(m, a, b):
    for i in range(8):
        m = swap(m)
        m = linear(m, a, b)
    return m


def run(kerberos, i):
    #
    #  kerberos: list<string>, list of team members' kerberos.
    #  i: index of returned element of message chain.
    #  Return: m_i, where m_0 = get_init_val(kerberos)
    #

    m = get_init_val(kerberos) #m_0
    k = key_gen(m) #k_1
    seen = {m: 1}
    repeats = 0


    # YOUR WORK GOES HERE
    for count in tqdm(range(i)):
        m = encrypt(m, *k)
        k = key_gen(m)
        if not m in seen:
            seen[m] = 0
            repeats -= 1
        seen[m] += 1
        repeats += 1
    print(f'num collisions: {repeats}')
    return m


def test():
	# Unit test. This should not raise errors if run() is implemented correctly!
	#
    assert(run(["kalai", "rivest"], 5000) == 11662425860819557635)
    assert(run(["lucas", "kyle", "andres"], 20000) == 5004391276101246881)
    print('tests passed')