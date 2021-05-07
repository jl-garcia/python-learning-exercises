class Connection:
    port = 55000
    conn_limit = 10
    connection_count = 0

    def __init__(self, host):
        if Connection.connection_count < Connection.conn_limit:
            Connection.connection_count += 1
            self.host = host
            self.port = Connection.port + 1
            Connection.port = self.port

    def close(self):
        Connection.remove_connection()

    @classmethod
    def get_next_port(cls):
        return Connection.port + 1

    @classmethod
    def get_connection_count(cls):
        return Connection.connection_count

    @classmethod
    def add_connection(cls):
        if Connection.connection_count < Connection.conn_limit:
            Connection.connection_count += 1
        else:
            print("Connection limit is reached")

    @classmethod
    def remove_connection(cls):
        if Connection.connection_count > 0:
            Connection.connection_count -= 1
        else:
            print("There is not any live connection")

    def __repr__(self):
        return f"{self.host}, {self.port}, {Connection.connection_count}"


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

    conn3 = Connection("my.local.net")
    print(f"Connection class limit: {conn3.__class__.conn_limit}")
    print(f"Connection class count: {conn3.__class__.connection_count}")

    print("---Removing connections")
    Connection.remove_connection()
    print(f"Connection class count: {conn3.__class__.connection_count}")

    print("---Getting the next port")
    print(f"Port: {Connection.get_next_port()}")

    print("---Adding a connection using an instance")
    conn3.add_connection()
    conn3.add_connection()
    conn3.add_connection()
    conn3.add_connection()
    print(f"Connection class count: {conn3.__class__.connection_count}")



if __name__ == "__main__":
    main()
