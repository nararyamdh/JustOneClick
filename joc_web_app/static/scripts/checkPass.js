let pass = document.getElementById("pass");
let confirm_pass = document.getElementById("confirm_pass");

let icon1 = document.getElementById("icon_1");
let icon2 = document.getElementById("icon_2");
let icon3 = document.getElementById("icon_3");
let icon4 = document.getElementById("icon_4");

let submit = document.querySelector(".submit");

let status1, status2, status3, status4 = false;

submit.setAttribute("disabled", "");

let con, val = "";

confirm_pass.addEventListener("input", () => {
    con = confirm_pass.value;

    if (status1 == true && status2 == true && status3 == true && status4 == true && con === val) {
        submit.removeAttribute("disabled");
    } else {
        submit.setAttribute("disabled", "");
    }
})

pass.addEventListener("input", () => {
    val = pass.value;

    if (val.length != 0) {
        if (val.length < 8) {
            icon1.src = "assets/icon/exlamation.svg";
            status1 = false;
        } else {
            icon1.src = "assets/icon/check.svg";
            status1 = true;
        }
        
        if (!(/[A-Z]/.test(val) && /[a-z]/.test(val))) {
            icon2.src = "assets/icon/exlamation.svg";
            status2 = false;
        } else {
            icon2.src = "assets/icon/check.svg";
            status2 = true;
        }

        if (!(/[0-9]/.test(val))) {
            icon3.src = "assets/icon/exlamation.svg";
            status3 = false;
        } else {
            icon3.src = "assets/icon/check.svg";
            status3 = true;
        }

        if (!(/[!@#$%^&*(),.?:;{}|]/.test(val))) {
            icon4.src = "assets/icon/exlamation.svg";
            status4 = false;
        } else {
            icon4.src = "assets/icon/check.svg";
            status4 = true;
        }

        if (status1 == true && status2 == true && status3 == true && status4 == true && con === val) {
            submit.removeAttribute("disabled");
        } else {
            submit.setAttribute("disabled", "");
        }
    } else {
        icon1.src = "assets/icon/question_mark.svg"
        icon2.src = "assets/icon/question_mark.svg"
        icon3.src = "assets/icon/question_mark.svg"
        icon4.src = "assets/icon/question_mark.svg"
    }
})