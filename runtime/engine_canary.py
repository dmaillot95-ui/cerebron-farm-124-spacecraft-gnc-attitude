import json,math,hashlib,pathlib,platform
# Torque-free symmetric rigid-body attitude canary: constant body-z angular rate.
I=(120.0,120.0,80.0); w=(0.0,0.0,0.01); dt=0.1; duration=100.0
# quaternion q=[w,x,y,z], exact constant-axis propagation used as independent analytic reference.
q=[1.0,0.0,0.0,0.0]
def mul(a,b):
 return [a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0]]
for _ in range(round(duration/dt)):
 th=w[2]*dt; dq=[math.cos(th/2),0,0,math.sin(th/2)]; q=mul(q,dq)
norm=math.sqrt(sum(v*v for v in q)); angle=2*math.atan2(q[3],q[0]); expected=w[2]*duration
energy=.5*sum(I[i]*w[i]**2 for i in range(3)); H=I[2]*w[2]
ok=abs(norm-1)<1e-12 and abs(angle-expected)<1e-10 and abs(energy-0.004)<1e-12 and abs(H-0.8)<1e-12
out={"farm":124,"engine":"python-rigid-body-attitude-canary","engine_version":platform.python_version(),"test":"TORQUE_FREE_Z_AXIS","inertia_kg_m2":I,"omega_rad_s":w,"duration_s":duration,"quaternion":q,"quaternion_norm":norm,"angle_rad":angle,"expected_angle_rad":expected,"rotational_energy_j":energy,"angular_momentum_kg_m2_s":H,"status":"REAL_ENGINE_CANARY_OK" if ok else "FAIL","epistemic_status":"ANALYTIC_RIGID_BODY_CANARY_NOT_HARDWARE_VALIDATION"}
raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f124_engine_canary.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
