from jupyter_server.extension.handler import ExtensionHandlerMixin


class TerminalsMixin(ExtensionHandlerMixin):
    @property
    def terminal_manager(self):
        return self.settings["terminal_manager"]  # type:ignore[attr-defined]
