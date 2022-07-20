from typing import Any

class Comment:
    content: Any
    author: Any
    height: Any
    width: Any
    def __init__(self, text, author, height: int = ..., width: int = ...) -> None: ...
    @property
    def parent(self): ...
    def __eq__(self, other): ...
    def __copy__(self): ...
    def bind(self, cell) -> None: ...
    def unbind(self) -> None: ...
    @property
    def text(self): ...
    @text.setter
    def text(self, value) -> None: ...
