document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("internshipForm");
  const responseMsg = document.getElementById("responseMsg");

  if (form && responseMsg) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      responseMsg.innerText = "Submitting...";
      responseMsg.style.color = "#555";

      const formData = {
        user_name: this.user_name.value,
        age: this.age.value,
        domain: this.domain.value,
        duration_months: this.duration_months.value,
      };

      try {
        const response = await fetch("/submit", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formData),
        });

        const result = await response.json();
        responseMsg.innerText = result.message || "Submitted!";
        responseMsg.style.color = "green";
        this.reset();
      } catch (err) {
        responseMsg.innerText = "Submission failed. Try again.";
        responseMsg.style.color = "red";
      }
    });
  }

  const searchBox = document.getElementById("search");
  if (searchBox) {
    searchBox.addEventListener("input", function () {
      const filter = this.value.toLowerCase();
      const rows = document.querySelectorAll("table tbody tr");
      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? "" : "none";
      });
    });
  }
});