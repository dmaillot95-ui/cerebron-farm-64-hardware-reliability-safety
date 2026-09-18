#!/usr/bin/env python3
import json,hashlib
REQ=("farm_id","domain","objective","method","evidence_level","validation","priority","task_type")
def enc(x):
 assert all(k in x for k in REQ);p={"language":"SPIRALIX-OMEGA","layer":"GLYPH-VECTOR-OMEGA","vector":{k:x[k] for k in REQ},"payload":x.get("payload",{})};p["sha256"]=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(",",":")).encode()).hexdigest();return p
def ok(p):
 q={k:v for k,v in p.items() if k!="sha256"};return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(",",":")).encode()).hexdigest()==p["sha256"]
if __name__=="__main__":
 x={"farm_id":64,"domain":"hardware-reliability-safety","objective":"interop self-test","method":"roundtrip","evidence_level":"E2","validation":"hash","priority":"normal","task_type":"interop"};p=enc(x);assert ok(p);print(json.dumps({"status":"VERIFIED","farm_id":64}))
