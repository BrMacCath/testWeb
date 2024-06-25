const openTabs = document.querySelectorAll("a span.mark");

const revealTab = function (e) {
  e.preventDefault();
  const clicked = e.target.closest("li.has-sub-menu");
  const target = clicked.querySelector("a span.mark").childnodes;
  const changeTabs = clicked.children;
  if (clicked.querySelector("a span.mark").innerText === "+") {
    clicked.querySelector("a span.mark").innerText = "-";
  } else {
    clicked.querySelector("a span.mark").innerText = "+";
  }
  [...changeTabs].forEach((t) => {
    if (t.nodeName === "UL") {
      if (t.classList.contains("hidden")) {
        t.classList.remove("hidden");
      } else {
        t.classList.add("hidden");
      }
    }
  });
};
openTabs.forEach((t) => t.addEventListener("click", revealTab));

// https://www.w3schools.com/howto/howto_js_display_checkbox_text.asp
