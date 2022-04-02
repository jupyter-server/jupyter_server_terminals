from .app import TerminalsExtensionApp


def _jupyter_server_extension_points():  # pragma: no cover
    return [
        {
            "module": "jupyter_server_terminals.app",
            "app": TerminalsExtensionApp,
        },
    ]
