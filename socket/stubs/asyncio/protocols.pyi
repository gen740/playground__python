class BaseProtocol:
    def connection_made(self, transport) -> None: ...
    def connection_lost(self, exc) -> None: ...
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...

class Protocol(BaseProtocol):
    def data_received(self, data) -> None: ...
    def eof_received(self) -> None: ...

class BufferedProtocol(BaseProtocol):
    def get_buffer(self, sizehint) -> None: ...
    def buffer_updated(self, nbytes) -> None: ...
    def eof_received(self) -> None: ...

class DatagramProtocol(BaseProtocol):
    def datagram_received(self, data, addr) -> None: ...
    def error_received(self, exc) -> None: ...

class SubprocessProtocol(BaseProtocol):
    def pipe_data_received(self, fd, data) -> None: ...
    def pipe_connection_lost(self, fd, exc) -> None: ...
    def process_exited(self) -> None: ...