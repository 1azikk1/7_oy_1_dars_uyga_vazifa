setTimeout(() => {
    document.querySelectorAll('.messages .alert').forEach(el => {
        el.classList.add('fade-out');
    });
}, 4000);

setTimeout(() => {
    const messagesDiv = document.querySelector('.messages');
    if (messagesDiv) {
        messagesDiv.remove();
    }
}, 5000);

//for form confirmation

document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('#deletecomment');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            const confirmation = confirm("Bu izohni o'chirishni xohlaysizmi?");
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });
});

//scroll button
//Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
scrollFunction();
};

function scrollFunction() {
if (
document.body.scrollTop > 20 ||
document.documentElement.scrollTop > 20
) {
mybutton.style.display = "block";
} else {
mybutton.style.display = "none";
}
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
document.body.scrollTop = 0;
document.documentElement.scrollTop = 0;
}

//dropdown button for student detail part
