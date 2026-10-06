import os
import socket


def file_transfer_client():
    filename = input("Enter the filename to send: ")

    # Check if the file exists locally before connecting or sending data
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found locally.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 12345))

        # Send the filename first
        client_socket.sendall(filename.encode())

        # Open and send the file contents in chunks
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                client_socket.sendall(chunk)

        print(f"File '{filename}' sent successfully.")

    except ConnectionRefusedError:
        print("Error: Could not connect to the server. Make sure the server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()


if __name__ == '__main__':
    file_transfer_client()