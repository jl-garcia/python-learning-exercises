class Connection:
    port = 55000
    conn_limit = 10
    connections = []

    def __init__(self, host):
        if len(self.connections) < self.conn_limit:
            self.host = host
            self.connections.append(self)
            self.port += len(self.connections)
        else:
            print("There is no room for more connections.")

    def close(self):
        self.connections.remove(self)

    def __repr__(self):
        return f"{self.host}, {self.port}, {len(self.connections)}"


def main():
    conn1 = Connection("localhost")
    print(f"Port: {conn1.port}")
    print(f"Connection count: {len(conn1.connections)}")
    print("...")
    conn2 = Connection("192.162.1.1")
    print(f"Port: {conn2.port}")
    print(f"Connection count: {len(conn2.connections)}")

    print("...")
    print(Connection)
    print(conn1)

    print("...")
    print(Connection.__dict__)
    print(conn1.__dict__)


if __name__ == "__main__":
    main()
