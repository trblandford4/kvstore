"""Minimal UDP key-value store supporting GET and SET operations."""
import socket

DEFAULT_PORT = 1111


def parse_request(message: bytes) -> tuple[bytes, bytes]:
    """Split incoming message into operation and payload."""
    op, payload = message.rstrip().split(b' ', 1)
    return op, payload


def handle_get(store: dict[bytes, bytes], key: bytes) -> bytes:
    return store[key]


def handle_set(store: dict[bytes, bytes], payload: bytes) -> bytes:
    key, value = payload.split(b'=', 1)
    store[key] = value
    return b'OK'


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', DEFAULT_PORT))

    store: dict[bytes, bytes] = {}

    while True:
        msg, addr = server_socket.recvfrom(4096)
        try:
            op, payload = parse_request(msg)

            if op == b'GET':
                response = handle_get(store, payload)
            elif op == b'SET':
                response = handle_set(store, payload)
            else:
                raise ValueError

            server_socket.sendto(response, addr)
        except ValueError:
            server_socket.sendto(b'ERROR invalid message structure', addr)
        except KeyError:
            server_socket.sendto(b'ERROR key not found', addr)


if __name__ == '__main__':
    main()
