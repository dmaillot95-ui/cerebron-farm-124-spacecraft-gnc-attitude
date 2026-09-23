import json,math,hashlib,pathlib,platform
I=80.;tau=.08;dt=.01;T=20.;n=int(T/dt);w=0.;theta=0.
for _ in range(n): w+=tau/I*dt; theta+=w*dt
w_ref=tau/I*T; theta_ref=.5*tau/I*T*T; ew=abs(w-w_ref); et=abs(theta-theta_ref);ok=ew<1e-12 and et<2e-4
out={"farm":124,"engine":"python-attitude-reference-suite-v2","test":"CONSTANT_TORQUE_AXIS","omega_rad_s":w,"omega_ref":w_ref,"theta_rad":theta,"theta_ref":theta_ref,"omega_error":ew,"theta_error":et,"status":"REFERENCE_SUITE_OK" if ok else "FAIL","scope":"ANALYTIC_GNC_REFERENCE_NOT_HARDWARE_VALIDATION","python":platform.python_version()};raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f124_reference_suite.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
