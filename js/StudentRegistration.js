function validateForm() {
  var studentName = document.getElementById("student-name").value;
  var studentEmail = document.getElementById("student-email").value;
  var studentPassword = document.getElementById("student-password").value;
  var confirmPassword = document.getElementById("student-password-confirm").value;

  // Check if required fields are empty
  if (studentName === "" || studentEmail === "" || studentPassword === "" || confirmPassword === "") {
    alert("All fields are required.");
    return false; // Prevent form submission
  }

  // Check if the password and confirm password fields match
  if (studentPassword !== confirmPassword) {
    alert("Passwords do not match.");
    return false; // Prevent form submission
  }

  // Email validation using regex
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(studentEmail)) {
    alert("Please enter a valid email address.");
    return false; // Prevent form submission
  }

  // If all checks pass, allow form submission
  return true;
}