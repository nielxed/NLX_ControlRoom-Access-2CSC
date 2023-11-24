# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['new_WGPtn_CRAcc2CSC_311023_23.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    name='new_WGPtn_CRAcc2CSC_311023_23',
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
    icon=['/Users/c_acadjiotis/Downloads/4017956.png'],
)
app = BUNDLE(
    exe,
    name='new_WGPtn_CRAcc2CSC_311023_23.app',
    icon='/Users/c_acadjiotis/Downloads/4017956.png',
    bundle_identifier=None,
)
