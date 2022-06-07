import enum
from _typeshed import Incomplete

LOG_THRESHOLD_FOR_CONNLOST_WRITES: int
ACCEPT_RETRY_DELAY: int
DEBUG_STACK_DEPTH: int
SSL_HANDSHAKE_TIMEOUT: float
SENDFILE_FALLBACK_READBUFFER_SIZE: Incomplete

class _SendfileMode(enum.Enum):
    UNSUPPORTED: Incomplete
    TRY_NATIVE: Incomplete
    FALLBACK: Incomplete
