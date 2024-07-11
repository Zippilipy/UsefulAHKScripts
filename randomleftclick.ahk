Suspend, On

~XButton2::Suspend, Toggle
~Shift & ~XButton2::Suspend, Toggle
~Ctrl & ~XButton2::Suspend, Toggle

~LButton::
    While GetKeyState("LButton", "P"){
    	Random, ClickDelay, 0, 300 ; 
        Sleep 50+ClickDelay ;  
	Click
    }
~Shift & ~LButton::
    While GetKeyState("LButton", "P"){
    	Random, ClickDelay, 0, 300 ; 
        Sleep 50+ClickDelay ;  
	Click
    }
~Ctrl & ~LButton::
    While GetKeyState("LButton", "P"){
    	Random, ClickDelay, 0, 300 ; 
        Sleep 50+ClickDelay ;  
	Click
    }

return