import os
import sys

from pydantic.dataclasses import dataclass


@dataclass
class PyLoxPrompt:
    had_error: bool = False

    def run(self) -> None:
        while True:
            sh_cmd = input("> ")

            if not sh_cmd:
                break

            PyLox.exec_lox(lox=sh_cmd)


@dataclass
class PyLoxFile:
    file_path: str
    had_error: bool = False

    def run(self) -> None:
        with open(self.file_path, "r") as file:
            content = file.read()
            PyLox.exec_lox(lox=content)


@dataclass(frozen=True)
class PyLox:
    run_strategy: PyLoxFile | PyLoxPrompt

    def run(self) -> None:
        self.run_strategy.run()

    @staticmethod
    def exec_lox(lox: str) -> None:
        return

    @staticmethod
    def error(line_num: int, message: str) -> None:
        print(f"[line {line_num}]: {message}")


def get_pylox(argv: list[str]) -> PyLox:
    if len(argv) > 2:
        raise Exception("Usage: pylox.py [script]")
    elif len(argv) == 2:
        if not os.path.exists(argv[1]):
            raise FileNotFoundError()
        else:
            return PyLox(run_strategy=PyLoxFile(file_path=argv[1]))
    else:
        return PyLox(run_strategy=PyLoxPrompt())


def main():
    pylox = get_pylox(argv=sys.argv)
    pylox.run()


if __name__ == "__main__":
    main()
