param([int]$OwnedProcess)
Add-Type @'
using System; using System.Text; using System.Runtime.InteropServices;
public class ReportWindow {
 public delegate bool EnumProc(IntPtr h, IntPtr p);
 [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc f,IntPtr p);
 [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h,out uint p);
 [DllImport("user32.dll",CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h,StringBuilder s,int n);
 [DllImport("user32.dll",CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr h,StringBuilder s,int n);
 [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h,int n);
}
'@
$callback=[ReportWindow+EnumProc]{param($handle,$unused)
 $owner=0;[void][ReportWindow]::GetWindowThreadProcessId($handle,[ref]$owner)
 if ($owner -eq $OwnedProcess) {
  $name=New-Object Text.StringBuilder 1024;$class=New-Object Text.StringBuilder 256
  [void][ReportWindow]::GetWindowText($handle,$name,1024)
  [void][ReportWindow]::GetClassName($handle,$class,256)
  Write-Host "$handle [$class] $name"
  if ($class.ToString() -eq 'OpusApp') {[void][ReportWindow]::ShowWindow($handle,5)}
 }
 return $true
}
[void][ReportWindow]::EnumWindows($callback,[IntPtr]::Zero)
