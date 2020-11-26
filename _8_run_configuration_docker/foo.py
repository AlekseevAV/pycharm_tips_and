import os


def is_run_in_docker() -> bool:
    return os.path.exists('/.dockerenv')


def main() -> None:
    if is_run_in_docker():
        msg = 'Run inside docker!'
    else:
        msg = r'Still not in docker ¯\_(ツ)_/¯'
    print(msg)


if __name__ == '__main__':
    main()
