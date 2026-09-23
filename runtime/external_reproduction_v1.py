import json,hashlib,pathlib,platform
import numpy as np
from scipy.integrate import solve_ivp
I=80.;tau=.08;T=20.
def f(t,y): return [y[1],tau/I]
sol=solve_ivp(f,[0,T],[0.,0.],rtol=1e-11,atol=1e-13,method="DOP853");theta,w=map(float,sol.y[:,-1]);wr=tau/I*T;tr=.5*tau/I*T*T;ok=abs(w-wr)<1e-10 and abs(theta-tr)<1e-10
out={"farm":124,"external_engine":"scipy.solve_ivp.DOP853","test":"CONSTANT_TORQUE_AXIS_EXTERNAL_REPRODUCTION","omega_rad_s":w,"theta_rad":theta,"omega_reference":wr,"theta_reference":tr,"status":"EXTERNAL_REPRODUCTION_OK" if ok else "FAIL","scope":"INDEPENDENT_NUMERICAL_SOLVER_NOT_HARDWARE_VALIDATION","python":platform.python_version()};raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f124_external_reproduction.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
