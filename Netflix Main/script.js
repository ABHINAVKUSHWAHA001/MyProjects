// Basic login/signup popup simulation
document.getElementById("loginBtn").addEventListener("click", () => {
  alert("Login page will open here.");
});

document.getElementById("signupBtn").addEventListener("click", () => {
  alert("Signup page will open here.");
});

// Scroll animation for future improvements
window.addEventListener("scroll", () => {
  const header = document.querySelector(".header");
  header.style.backgroundColor =
    window.scrollY > 50 ? "rgba(0,0,0,0.95)" : "rgba(0,0,0,0.8)";
});
