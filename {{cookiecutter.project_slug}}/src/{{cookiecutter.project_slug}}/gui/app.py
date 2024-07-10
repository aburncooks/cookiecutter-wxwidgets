import wx


class {{cookiecutter.project_short_name}}App(wx.App):
    """
    A class for {{cookiecutter.project_short_name}}App
    """
    def __init__(self) -> None:
        """
        Create the {{cookiecutter.project_short_name}}App app
        """
        super({{cookiecutter.project_short_name}}App, self).__init__()
        self.app_name = "{{cookiecutter.project_name}}"
