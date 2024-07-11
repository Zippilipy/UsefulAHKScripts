#MaxThreadsPerHotkey 3

F2::
Toggle := !Toggle
Loop
{
	if (!Toggle)
		Break
	Click
	Sleep 83 ; Make this number higher for slower clicks, lower for faster.
}
Return