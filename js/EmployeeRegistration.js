function validateForm() {
  var employeeId = document.getElementById("employee-id").value;
  var employeeName = document.getElementById("employee-name").value;
  var employeeEmail = document.getElementById("employee-email").value;
  var employeeDesignation = document.getElementById("employee-designation").value;
  var employeePassword = document.getElementById("employee-password").value;
  var confirmPassword = document.getElementById("employee-password-confirm").value;

  // Check if required fields are empty
  if (employeeId === "" || employeeName === "" || employeeDesignation === "" || employeePassword === "" || confirmPassword === "") {
    alert("All fields are required.");
    return false; // Prevent form submission
  }

  // Check if the password and confirm password fields match
  if (employeePassword !== confirmPassword) {
    alert("Passwords do not match.");
    return false; // Prevent form submission
  }

  // Email validation using regex
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(employeeEmail)) {
    alert("Please enter a valid email address.");
    return false; // Prevent form submission
  }

  // If all checks pass, allow form submission
  return true;
}