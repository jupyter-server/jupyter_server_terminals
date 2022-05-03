from ._version import __version__  # noqa:F401

try:
    from .app import TerminalsExtensionApp
except ModuleNotFoundError:
    import warnings

    warnings.warn("Could not import submodules")


def _jupyter_server_extension_points():  # pragma: no cover
    return [
        {
            "module": "jupyter_server_terminals.app",
            "app": TerminalsExtensionApp,
        },
    ]
