#!/usr/bin/env python3
import datetime,hashlib,json,pathlib,subprocess,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
audit=pathlib.Path('/opt/csjs/commands/unity1-classics-public-boundary-audit')
if audit.is_file(): subprocess.check_call([str(audit),'--project',ROOT.name])
files=[x for x in subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0') if x]
for rel in files:
 if rel=='private-input' or rel.startswith('private-input/') or '/private-input/' in rel: raise SystemExit('ERROR: tracked private-input boundary violation')
entries=[x for x in subprocess.check_output(['git','ls-files','-s','-z'],cwd=ROOT).decode().split('\0') if x]
for rec in entries:
 mode=rec.split(None,1)[0]
 if mode not in {'100644','100755'}: raise SystemExit('ERROR: tracked symlink/submodule/special entry prohibited in Classics context export')
sha=git('rev-parse','--short=8','HEAD'); stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
out=pathlib.Path('/srv/csjs/artifacts')/f'CHATGPT_{ROOT.name.upper().replace("-","_")}_CONTEXT_{sha}_{stamp}.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for rel in sorted(files):
  p=ROOT/rel
  if p.is_file(): z.write(p,rel)
 meta={'schema_version':1,'project_id':ROOT.name,'head':git('rev-parse','HEAD'),'tracked_files':len(files),'private_content_included':False}
 z.writestr('CONTEXT_MANIFEST.json',json.dumps(meta,indent=2)+'\n')
print(out)
