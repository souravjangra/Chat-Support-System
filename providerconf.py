from contextlib import contextmanager
from bocadillo import provider

@provider(scope="app")
async def clients() -> set:
    return set()

@provider
async def save_client(clients):
    @contextmanager
    def _save(ws):
        clients.add(ws)
        try:
            yield ws
        finally:
            clients.remove(ws)

    return _save