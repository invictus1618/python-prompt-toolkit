"""
Interface for an output.
"""
from abc import ABCMeta, abstractmethod

from prompt_toolkit.layout.screen import Size
from prompt_toolkit.styles import Attrs

from .ColorDepth import ColorDepth

__all__ = [
    'Output',
    'DummyOutput',
]


class Output(metaclass=ABCMeta):
    """
    Base class defining the output interface for a
    :class:`~prompt_toolkit.renderer.Renderer`.

    Actual implementations are
    :class:`~prompt_toolkit.terminal.vt100_output.Vt100_Output` and
    :class:`~prompt_toolkit.terminal.win32_output.Win32Output`.
    """
    @abstractmethod
    def fileno(self) -> int:
        " Return the file descriptor to which we can write for the output. "

    @abstractmethod
    def encoding(self) -> str:
        """
        Return the encoding for this output, e.g. 'utf-8'.
        (This is used mainly to know which characters are supported by the
        output the data, so that the UI can provide alternatives, when
        required.)
        """

    @abstractmethod
    def write(self, data: str) -> None:
        " Write text (Terminal escape sequences will be removed/escaped.) "

    @abstractmethod
    def write_raw(self, data: str) -> None:
        " Write text. "

    @abstractmethod
    def set_title(self, title: str) -> None:
        " Set terminal title. "

    @abstractmethod
    def clear_title(self) -> None:
        " Clear title again. (or restore previous title.) "

    @abstractmethod
    def flush(self) -> None:
        " Write to output stream and flush. "

    @abstractmethod
    def erase_screen(self) -> None:
        """
        Erases the screen with the background colour and moves the cursor to
        home.
        """

    @abstractmethod
    def enter_alternate_screen(self) -> None:
        " Go to the alternate screen buffer. (For full screen applications). "

    @abstractmethod
    def quit_alternate_screen(self) -> None:
        " Leave the alternate screen buffer. "

    @abstractmethod
    def enable_mouse_support(self) -> None:
        " Enable mouse. "

    @abstractmethod
    def disable_mouse_support(self) -> None:
        " Disable mouse. "

    @abstractmethod
    def erase_end_of_line(self) -> None:
        """
        Erases from the current cursor position to the end of the current line.
        """

    @abstractmethod
    def erase_down(self) -> None:
        """
        Erases the screen from the current line down to the bottom of the
        screen.
        """

    @abstractmethod
    def reset_attributes(self) -> None:
        " Reset color and styling attributes. "

    @abstractmethod
    def set_attributes(self, attrs: Attrs, color_depth: ColorDepth) -> None:
        " Set new color and styling attributes. "

    @abstractmethod
    def disable_autowrap(self) -> None:
        " Disable auto line wrapping. "

    @abstractmethod
    def enable_autowrap(self) -> None:
        " Enable auto line wrapping. "

    @abstractmethod
    def cursor_goto(self, row: int = 0, column: int = 0) -> None:
        " Move cursor position. "

    @abstractmethod
    def cursor_up(self, amount: int) -> None:
        " Move cursor `amount` place up. "

    @abstractmethod
    def cursor_down(self, amount: int) -> None:
        " Move cursor `amount` place down. "

    @abstractmethod
    def cursor_forward(self, amount: int) -> None:
        " Move cursor `amount` place forward. "

    @abstractmethod
    def cursor_backward(self, amount: int) -> None:
        " Move cursor `amount` place backward. "

    @abstractmethod
    def hide_cursor(self) -> None:
        " Hide cursor. "

    @abstractmethod
    def show_cursor(self) -> None:
        " Show cursor. "

    def ask_for_cpr(self) -> None:
        """
        Asks for a cursor position report (CPR).
        (VT100 only.)
        """

    def bell(self) -> None:
        " Sound bell. "

    def enable_bracketed_paste(self) -> None:
        " For vt100 only. "

    def disable_bracketed_paste(self) -> None:
        " For vt100 only. "

    def scroll_buffer_to_prompt(self) -> None:
        " For Win32 only. "


class DummyOutput(Output):
    """
    For testing. An output class that doesn't render anything.
    """
    def fileno(self):
        " There is no sensible default for fileno(). "
        raise NotImplementedError

    def encoding(self) -> str:
        return 'utf-8'

    def write(self, data): pass
    def write_raw(self, data): pass
    def set_title(self, title): pass
    def clear_title(self): pass
    def flush(self): pass
    def erase_screen(self): pass
    def enter_alternate_screen(self): pass
    def quit_alternate_screen(self): pass
    def enable_mouse_support(self): pass
    def disable_mouse_support(self): pass
    def erase_end_of_line(self): pass
    def erase_down(self): pass
    def reset_attributes(self): pass
    def set_attributes(self, attrs, color_depth): pass
    def disable_autowrap(self): pass
    def enable_autowrap(self): pass
    def cursor_goto(self, row=0, column=0): pass
    def cursor_up(self, amount): pass
    def cursor_down(self, amount): pass
    def cursor_forward(self, amount): pass
    def cursor_backward(self, amount): pass
    def hide_cursor(self): pass
    def show_cursor(self): pass
    def ask_for_cpr(self): pass
    def bell(self): pass
    def enable_bracketed_paste(self): pass
    def disable_bracketed_paste(self): pass
    def scroll_buffer_to_prompt(self): pass

    def get_size(self) -> Size:
        return Size(rows=40, columns=80)

    def get_rows_below_cursor_position(self) -> int:
        return 40
