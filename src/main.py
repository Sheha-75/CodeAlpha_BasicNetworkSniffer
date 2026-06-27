from sniffer import start_sniffer


def main():

    try:
        start_sniffer()

    except KeyboardInterrupt:
        print("\n\nSniffer stopped successfully.")

    except PermissionError:
        print("\nRun the program with sudo.")

    except Exception as error:
        print(f"\nUnexpected Error: {error}")


if __name__ == "__main__":
    main()
