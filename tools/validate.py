#!/usr/bin/env python3
import pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def run(*a):
 p=subprocess.run(a,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=False)
 if p.returncode: print(p.stdout); raise SystemExit(p.returncode)
 return p.stdout
tracked=[x for x in run('git','ls-files','-z').split('\0') if x]
bad=[x for x in tracked if x=='private-input' or x.startswith('private-input/') or '/private-input/' in x]
if bad: print('FAIL: private-input tracked: '+', '.join(bad)); raise SystemExit(1)
staged=run('git','ls-files','-s','-z')
for rec in [x for x in staged.split('\0') if x]:
 mode=rec.split(None,1)[0]
 if mode not in {'100644','100755'}: print('FAIL: unsupported tracked Git entry mode '+mode); raise SystemExit(1)
audit=pathlib.Path('/opt/csjs/commands/unity1-classics-public-boundary-audit')
if audit.is_file():
 p=subprocess.run([str(audit),'--project',ROOT.name],text=True)
 if p.returncode: raise SystemExit(p.returncode)
print(f'CLASSICS PROJECT VALIDATION: PASS project={ROOT.name} tracked={len(tracked)}')
