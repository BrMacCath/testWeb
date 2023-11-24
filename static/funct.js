function myFunction() {
    var fixButtons = document.querySelectorAll("li.has-sub-menu a span");

    fixButtons.forEach(t => {
        t.addEventListener("click", function(){
        t.innerHTML = "-";
        }
        )
    });
}
// https://www.w3schools.com/howto/howto_js_display_checkbox_text.asp
