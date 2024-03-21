# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['D:/Dev/Xuchetucraft/dist/lib'],
    binaries=[],
    datas=[('D:/Dev/Xuchetucraft/api/credentials.json', 'api'), ('D:/Dev/Xuchetucraft/assets/panda.ico', 'assets'), ('D:/Dev/Xuchetucraft/assets/novaskin-wallpaper-llama_cut.jpg', 'assets'), ('D:/Dev/Xuchetucraft/assets/xuchetucraft_logo.jpg', 'assets')],
    hiddenimports=['api', 'interface'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\Dev\\Xuchetucraft\\assets\\panda.ico'],
)
