Add-Type @'
using System; using System.Runtime.InteropServices; using System.Text;
public class TtpWindows {
 public delegate bool Callback(IntPtr h,IntPtr l);
 [DllImport("user32.dll")] public static extern bool EnumWindows(Callback f,IntPtr l);
 [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h,out uint p);
 [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h,StringBuilder s,int n);
 [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h,int n);
}
'@
[TtpWindows]::EnumWindows({param($h,$l) [uint32]$p=0;[void][TtpWindows]::GetWindowThreadProcessId($h,[ref]$p);if($p -eq 60236){$s=New-Object Text.StringBuilder 512;[void][TtpWindows]::GetWindowText($h,$s,512);if($s.Length -gt 0){Write-Output "$h $s";[void][TtpWindows]::ShowWindow($h,5)}};return $true},[IntPtr]::Zero)
