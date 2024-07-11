Suspend, On

~XButton2::Suspend, Toggle
~Shift & ~XButton2::Suspend, Toggle
~Ctrl & ~XButton2::Suspend, Toggle

~Shift::
    alt := not alt
    if (alt)
    {
        Send, {Shift Down}
    }
    else
    {
        Send, {Shift Up}
    }