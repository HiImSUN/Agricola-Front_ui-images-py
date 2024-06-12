# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=['/Users/seonhukim/Documents/GitHub/Agricola-Front ui-images-py/Agricola_Front/Agricola_Back','/Users/seonhukim/Documents/GitHub/Agricola-Front_ui-images-py/Agricola_Front/Agricola_Back/Agricola/behavior','/Users/seonhukim/Documents/GitHub/Agricola-Front_ui-images-py/Agricola_Front/Agricola_Back/Agricola/entity'],
    binaries=[],
    datas=[('data', 'data'), ('Agricola_Back', 'Agricola_Back'), ('list_import.py', '.'), ('round_event.py', '.')],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)


pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Agricola_Launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='Agricola_Launcher.app',
    icon='',
    bundle_identifier=None,
)
