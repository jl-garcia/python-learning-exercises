class Connection:
    port = 55000
    conn_limit = 10
    connection_count = 0

    def __init__(self, host):
        self.host = host
        self.connection_count = self.connection_count + 1

    def close(self):
        self.connection_count = self.connection_count - 1

    def __repr__(self):
        return f"{self.host}, {self.port}, {self.connection_count}"


def main():
    conn1 = Connection("localhost")
    print(f"Port: {conn1.port}")
    print(f"Connection count: {conn1.connection_count}")
    print("...")
    conn2 = Connection("192.162.1.1")
    print(f"Port: {conn2.port}")
    print(f"Connection count: {conn2.connection_count}")

    print("...")
    print(Connection)
    print(conn1)

    print("...")
    print(Connection.__dict__)
    print(conn1.__dict__)


if __name__ == "__main__":
    main()
