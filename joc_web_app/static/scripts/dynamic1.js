let textboxes = document.querySelectorAll(".input-1");
let containers = document.querySelectorAll(".textbox");
let icons = document.querySelectorAll(".icon");

textboxes.forEach((textbox, i) => {
  textbox.addEventListener("focus", () => {
    icons[i].src = "/Volumes/AryaMD/Me/Project/JustOneClick/assets/icon/email_f.svg";
    containers[i].style.border = "2px solid rgb(17, 137, 243)";
  });

  textbox.addEventListener("blur", () => {
    icons[i].src = "/Volumes/AryaMD/Me/Project/JustOneClick/assets/icon/email.svg";
    containers[i].style.border = "1px solid #dddddd";
  });
});

let preloader = document.querySelector(".preloader");
window.onload = function() {
  preloader.style.display = "None";
}