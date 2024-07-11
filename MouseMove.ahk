; Define state variables
global toggle := true
global right_click_to_d := true

; Toggle function for Mouse5
ToggleRightClick() {
    global right_click_to_d
    right_click_to_d := !right_click_to_d
}

; Toggle function for Mouse4
ToggleScript() {
    global toggle
    toggle := !toggle
}

; Remap right click to 'd' or 'a' when toggle is on
*RButton::
    global toggle, right_click_to_d
    if (toggle) {
        if (right_click_to_d) {
            SendInput {d Down}
        } else {
            SendInput {a Down}
        }
        while GetKeyState("RButton", "P") {
            Sleep, 10
        }
        if (right_click_to_d) {
            SendInput {d Up}
        } else {
            SendInput {a Up}
        }
    } else {
        ; If the script is toggled off, perform the normal right-click action
        MouseClick, right
    }
return

; Detect Mouse5 (XButton2) press and toggle right click remap
~XButton2::
    ToggleRightClick()
return

; Detect Mouse4 (XButton1) press and toggle script on/off
~XButton1::
    ToggleScript()
return
