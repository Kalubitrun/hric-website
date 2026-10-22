/* Haridwar Rai Inter College — proposal site
   Minimal JS: footer year + WhatsApp enquiry form. No dependencies. */

(function () {
  "use strict";

  var WA_NUMBER = "919451570855";

  // Footer year
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = String(new Date().getFullYear());

  // Enquiry form -> opens WhatsApp with a prefilled message (no backend needed)
  var form = document.getElementById("enquiry-form");
  if (!form) return;

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var name = (form.querySelector("#f-name") || {}).value || "";
    var phone = (form.querySelector("#f-phone") || {}).value || "";
    var cls = (form.querySelector("#f-class") || {}).value || "";
    var msg = (form.querySelector("#f-msg") || {}).value || "";

    name = name.trim();
    phone = phone.trim();

    if (!name || !phone) {
      alert("कृपया नाम और मोबाइल नंबर भरें।");
      return;
    }

    var digits = phone.replace(/\D/g, "");
    if (digits.length !== 10) {
      alert("कृपया 10 अंकों का मोबाइल नंबर भरें।");
      return;
    }

    var lines = [
      "नमस्ते, मुझे प्रवेश के बारे में जानकारी चाहिए।",
      "",
      "नाम: " + name,
      "मोबाइल: " + digits,
      "कक्षा: " + cls
    ];
    if (msg.trim()) lines.push("संदेश: " + msg.trim());

    var url = "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(lines.join("\n"));
    window.open(url, "_blank", "noopener");
  });
})();
