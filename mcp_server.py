import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('Browser Automation API (Headless Sessions)')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "session_create",
    "method": "POST",
    "path": "/session/create",
    "description": "V1 Session Create"
  },
  {
    "name": "interact",
    "method": "POST",
    "path": "/interact",
    "description": "V1 Interact"
  },
  {
    "name": "session_list",
    "method": "POST",
    "path": "/session/list",
    "description": "V1 Session List"
  },
  {
    "name": "session_delete",
    "method": "POST",
    "path": "/session/delete",
    "description": "V1 Session Delete"
  },
  {
    "name": "browse",
    "method": "POST",
    "path": "/browse",
    "description": "V1 Browse"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
