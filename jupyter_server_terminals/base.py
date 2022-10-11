try:
    from jupyter_server.extension.handler import ExtensionHandlerMixin
except ModuleNotFoundError:
    raise ModuleNotFoundError("Jupyter Server must be installed to use this extension.")


class TerminalsMixin(ExtensionHandlerMixin):
    @property
    def terminal_manager(self):
        return self.settings["terminal_manager"]  # type:ignore[attr-defined]
