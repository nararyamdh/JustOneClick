let dialog = document.querySelector(".dialog");

let AddPaymentMethodDialog = document.getElementById("AddPaymentMethodDialog");
let EditPaymentData = document.getElementById("EditPaymentData");

dialog.style.display = "none";

function closeDialog() {
    dialog.style.display = "none";
}

function AddPaymentMethodDialog_open() {
    dialog.style.display = "flex";
    
    EditPaymentData.style.display = "none";
    AddPaymentMethodDialog.style.display = "block";
}

function EditPaymentData_open() {
    dialog.style.display = "flex";
    
    EditPaymentData.style.display = "block";
    AddPaymentMethodDialog.style.display = "none";
}