[Setup]
AppId={{A1D5E4B2-9F8B-4D7B-9A0A-1C2D3E4F5A6B}}
AppName=OverlayApp
AppVersion=1.0.0
AppPublisher=Blue
AppPublisherURL=https://bluetccth.github.io/ProfileMe
AppSupportURL=https://bluetccth.github.io/ProfileMe
AppUpdatesURL=https://bluetccth.github.io/ProfileMe
DefaultDirName={autopf}\OverlayApp
DefaultGroupName=OverlayApp
DisableProgramGroupPage=yes
PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=installer_output
OutputBaseFilename=OverlayApp_Setup
SetupIconFile=assets\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64
UninstallDisplayIcon={app}\Overlay App.exe

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "dist\Overlay App.exe"; DestDir: "{app}"; Flags: ignoreversion restartreplace

[Icons]
Name: "{group}\OverlayApp"; Filename: "{app}\Overlay App.exe"
Name: "{autodesktop}\OverlayApp"; Filename: "{app}\Overlay App.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Overlay App.exe"; Description: "Launch OverlayApp"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{localappdata}\OverlayApp"

[Code]
// ฟังก์ชันปิด Overlay App.exe ถ้ามันเปิดอยู่
function InitializeSetup(): Boolean;
var
  ResultCode: Integer;
begin
  // ปิด Overlay App.exe แบบ force
  Exec('taskkill', '/F /IM Overlay App.exe', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  Result := True;
end;