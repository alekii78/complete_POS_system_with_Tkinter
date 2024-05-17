from cx_Freeze import setup, Executable, sys

includefiles = ['icon.ico']
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "billingSystem",
     "TARGETDIR",
     "[TARGETDIR]\billingSystem.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version="0.0.1",
    description="alexbillingsystem",
    author="ALEXANDER NJUGUNA MIRII",
    name="ALEXIA TECH BILLING SYSTEM ",
    options={'build_exe': {'include_files': includefiles}, 'bdist_msi': bdist_msi_options, },
    executables=[
        Executable(
            script="billingSystem.py",
            base=base,
            icon='icon.ico',
        )
    ]
)
